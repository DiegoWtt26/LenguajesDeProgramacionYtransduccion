#!/usr/bin/env python3
# ============================================================
# Tarea #1 - Diapositiva 11 TAL CUAL
# Gramatica: E -> E + T | T ;  T -> T * F | F ;  F -> id|num|(E)
# Uso (Linux):
#   python3 main.py casos.txt          (lee un .txt, uno por linea)
#   python3 main.py "2 + 3 * 4"
#   python3 main.py "a + b * c | a=2 b=3 c=4"
#   python3 main.py                    (usa casos.txt por defecto)
# Requisito:  pip3 install antlr4-python3-runtime==4.13.2
# Generar parser (solo si se modifica Expr11.g4):
#   ./generar.sh
# ============================================================
import os
import sys
from antlr4 import CommonTokenStream, InputStream
from antlr4.tree.Tree import TerminalNode
from antlr4.tree.Trees import Trees
from antlr4.error.ErrorListener import ErrorListener

from Expr11Lexer import Expr11Lexer
from Expr11Parser import Expr11Parser
from Expr11Visitor import Expr11Visitor


class Silencio(ErrorListener):
    """Evita que ANTLR imprima errores por stderr; los contamos nosotros."""
    def __init__(self):
        self.n = 0

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.n += 1


class EvalVisitor(Expr11Visitor):
    """Evaluador: necesita tabla de simbolos para los id."""
    def __init__(self, variables=None):
        self.vars = variables or {}

    def visitProg(self, ctx):
        return self.visit(ctx.e())

    def visitSuma(self, ctx):
        return self.visit(ctx.e()) + self.visit(ctx.t())

    def visitA_T(self, ctx):
        return self.visit(ctx.t())

    def visitMult(self, ctx):
        return self.visit(ctx.t()) * self.visit(ctx.f())

    def visitA_F(self, ctx):
        return self.visit(ctx.f())

    def visitNum(self, ctx):
        return int(ctx.NUM().getText())

    def visitId(self, ctx):
        nombre = ctx.ID().getText()
        if nombre not in self.vars:
            raise ValueError(f"identificador sin valor: {nombre!r} "
                             f"(usa formato 'expr | {nombre}=valor' en el .txt)")
        return self.vars[nombre]

    def visitParens(self, ctx):
        return self.visit(ctx.e())


def ascii_parse_tree(nodo, parser, prefijo="", es_ultimo=True, lineas=None):
    """Dibuja CUALQUIER parse tree en ASCII (reglas + tokens)."""
    if lineas is None:
        lineas = []
    if isinstance(nodo, TerminalNode):
        etiqueta = nodo.getText()
    else:
        etiqueta = parser.ruleNames[nodo.getRuleIndex()]
    marca = "`-- " if es_ultimo else "|-- "
    lineas.append(prefijo + marca + etiqueta)
    extension = prefijo + ("    " if es_ultimo else "|   ")
    n = nodo.getChildCount()
    for i in range(n):
        ascii_parse_tree(nodo.getChild(i), parser, extension, i == n - 1, lineas)
    return lineas


def parsear_vars(texto_vars):
    """'a=2 b=3' -> {'a':2,'b':3}. Acepta comas o espacios."""
    vars_ = {}
    if not texto_vars:
        return vars_
    for tok in texto_vars.replace(",", " ").split():
        if "=" in tok:
            k, v = tok.split("=", 1)
            k, v = k.strip(), v.strip()
            try:
                vars_[k] = int(v)
            except ValueError:
                try:
                    vars_[k] = float(v)
                except ValueError:
                    vars_[k] = v
    return vars_


def separar_linea(linea):
    """'a + b * c | a=2 b=3' -> ('a + b * c', {'a':2,...}). Sin '|' -> (linea, {})."""
    if "|" in linea:
        expr, vars_txt = linea.split("|", 1)
        return expr.strip(), parsear_vars(vars_txt.strip())
    return linea.strip(), {}


def analizar(texto, variables=None, num=None):
    variables = variables or {}
    etiqueta = f"[{num}] " if num is not None else ""
    print(f"{etiqueta}Entrada    : {texto}" + (f"   vars={variables}" if variables else ""))
    lexer = Expr11Lexer(InputStream(texto))
    lexer.removeErrorListeners()
    err_lex = Silencio()
    lexer.addErrorListener(err_lex)
    tokens = CommonTokenStream(lexer)
    parser = Expr11Parser(tokens)
    parser.removeErrorListeners()
    err_par = Silencio()
    parser.addErrorListener(err_par)
    tree = parser.prog()
    n_errores = err_lex.n + err_par.n + parser.getNumberOfSyntaxErrors()
    if n_errores > 0:
        print("  Estado     : RECHAZADA (error de sintaxis)")
        print("  Evaluacion : -- (no se evalua lo rechazado)")
        print("-" * 60)
        return False
    print("  Estado     : ACEPTADA")
    lisp = Trees.toStringTree(tree, None, parser)
    print(f"  Parse tree : {lisp}")
    for linea in ascii_parse_tree(tree, parser):
        print("    " + linea)
    try:
        valor = EvalVisitor(variables).visit(tree)
    except ValueError as ex:
        print(f"  Evaluacion : ERROR semantico: {ex}")
        print("-" * 60)
        return True  # aceptada sintacticamente, aunque sin valor semantico
    print(f"  Evaluacion : {valor}")
    print("-" * 60)
    return True


def procesar_archivo(ruta):
    print(f"=== Tarea #1 - Diapositiva 11 TAL CUAL | archivo: {ruta} ===\n")
    ok = total = 0
    with open(ruta, encoding="utf-8") as f:
        n = 0
        for cruda in f:
            linea = cruda.strip()
            if not linea or linea.startswith("#"):
                continue
            n += 1
            total += 1
            expr, vars_ = separar_linea(linea)
            if analizar(expr, vars_, n):
                ok += 1
    print(f"Resumen: {ok}/{total} ACEPTADAS, {total - ok}/{total} RECHAZADAS.")
    print("Nota: '2 + 3 - 4' y '2 + 3 * (4 - 5)' son RECHAZADAS porque la")
    print("gramatica TAL CUAL solo define '+' y '*', sin '-'. Eso es lo correcto.")


def main():
    base = os.path.dirname(os.path.abspath(__file__))
    defecto = os.path.join(base, "casos.txt")
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if arg.lower().endswith(".txt") and os.path.isfile(arg):
                procesar_archivo(arg)
            elif os.path.isfile(os.path.join(base, arg)):
                procesar_archivo(os.path.join(base, arg))
            else:
                expr, vars_ = separar_linea(arg)
                analizar(expr, vars_)
    else:
        if os.path.isfile(defecto):
            procesar_archivo(defecto)
        else:
            analizar("2 + 3 * 4")


if __name__ == "__main__":
    main()
