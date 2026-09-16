#!/usr/bin/env python3
# ============================================================
# Tarea #2 - Diapositivas 12 (Parse Tree) y 13 (AST)
# Comprueba las diferentes formas de AST para la gramatica de
# expresiones con TAL CUAL diapo 11. Cada caso del .txt dice
# ACEPTADA/RECHAZADA y se evalua.
#
# Uso (Linux):
#   python3 main.py casos.txt       (lee un .txt, uno por linea)
#   python3 main.py "3 + 4 * 5"
#   python3 main.py "a + b * c | a=2 b=3 c=4"
#   python3 main.py                 (usa casos.txt por defecto)
#
# Requisito: pip3 install antlr4-python3-runtime==4.13.2
# Regenerar (solo si se modifica Expr12.g4): ./generar.sh
# ============================================================
import json
import os
import sys
from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Trees import Trees

from Expr12Lexer import Expr12Lexer
from Expr12Parser import Expr12Parser
from Expr12Visitor import Expr12Visitor


class Silencio(ErrorListener):
    def __init__(self):
        self.n = 0

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.n += 1


# ---------- AST compacto (diapo 13): solo operadores/operandos ----------
class Nodo:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

    def tupla(self):
        # Forma 1: tupla anidada  ('+', '3', ('*', '4', '5'))
        if self.izq is None and self.der is None:
            return self.valor
        return (self.valor, self.izq.tupla(), self.der.tupla())

    def dicc(self):
        # Forma 2: dict/JSON  {"op": "+", ...} / {"num": "3"} / {"id": "a"}
        if self.izq is None and self.der is None:
            clave = "num" if self.valor.lstrip("-").isdigit() else "id"
            return {clave: self.valor}
        return {"op": self.valor, "izq": self.izq.dicc(), "der": self.der.dicc()}

    def evaluar(self, variables=None):
        variables = variables or {}
        if self.izq is None:
            try:
                return int(self.valor)
            except ValueError:
                if self.valor not in variables:
                    raise ValueError(f"identificador sin valor: {self.valor!r}")
                return variables[self.valor]
        a, b = self.izq.evaluar(variables), self.der.evaluar(variables)
        return {"+": a + b, "-": a - b, "*": a * b, "/": a // b}[self.valor]

    def ascii(self, prefijo="", es_ultimo=True, lineas=None):
        # Forma 3: dibujo ASCII del arbol
        if lineas is None:
            lineas = []
        marca = "`-- " if es_ultimo else "|-- "
        lineas.append(prefijo + marca + str(self.valor))
        ext = prefijo + ("    " if es_ultimo else "|   ")
        hijos = [h for h in (self.izq, self.der) if h is not None]
        for i, h in enumerate(hijos):
            h.ascii(ext, i == len(hijos) - 1, lineas)
        return lineas


class AASTVisitor(Expr12Visitor):
    """Convierte el Parse Tree en AST eliminando E/T/F intermedios."""
    def visitProg(self, ctx):
        return self.visit(ctx.e())

    def visitSuma(self, ctx):
        return Nodo("+", self.visit(ctx.e()), self.visit(ctx.t()))

    def visitA_T(self, ctx):
        return self.visit(ctx.t())

    def visitMult(self, ctx):
        return Nodo("*", self.visit(ctx.t()), self.visit(ctx.f()))

    def visitA_F(self, ctx):
        return self.visit(ctx.f())

    def visitNum(self, ctx):
        return Nodo(ctx.NUM().getText())

    def visitId(self, ctx):
        return Nodo(ctx.ID().getText())

    def visitParens(self, ctx):
        return self.visit(ctx.e())


def parsear_vars(texto_vars):
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
                vars_[k] = v
    return vars_


def separar_linea(linea):
    if "|" in linea:
        expr, vars_txt = linea.split("|", 1)
        return expr.strip(), parsear_vars(vars_txt.strip())
    return linea.strip(), {}


def analizar(texto, variables=None, num=None):
    variables = variables or {}
    etiqueta = f"[{num}] " if num is not None else ""
    print("=" * 64)
    print(f"{etiqueta}ENTRADA: {texto}" + (f"   vars={variables}" if variables else ""))
    print("=" * 64)
    lexer = Expr12Lexer(InputStream(texto))
    lexer.removeErrorListeners()
    err_lex = Silencio()
    lexer.addErrorListener(err_lex)
    parser = Expr12Parser(CommonTokenStream(lexer))
    parser.removeErrorListeners()
    err_par = Silencio()
    parser.addErrorListener(err_par)
    tree = parser.prog()
    n_err = err_lex.n + err_par.n + parser.getNumberOfSyntaxErrors()
    if n_err > 0:
        print("Estado     : RECHAZADA (error de sintaxis)")
        print("Evaluacion : -- (no se evalua lo rechazado)\n")
        return False

    print("Estado     : ACEPTADA")

    # ---- 1. PARSE TREE (diapo 12): estructura completa ----
    print("\n[1] PARSE TREE (diapositiva 12) - conserva E, T, F:")
    print(f"    {Trees.toStringTree(tree, None, parser)}")

    # ---- 2. AST (diapo 13): solo operadores y operandos ----
    ast = AASTVisitor().visit(tree)
    print("\n[2] AST (diapositiva 13) - solo operadores y operandos:")
    print("\n  Forma A - ASCII (igual al dibujo de la diapo 13):")
    print(f"    {ast.valor}")
    hijos = [h for h in (ast.izq, ast.der) if h is not None]
    for i, h in enumerate(hijos):
        for linea in h.ascii("    ", i == len(hijos) - 1):
            print("   " + linea)
    print("\n  Forma B - tupla anidada:")
    print(f"    {ast.tupla()}")
    print("\n  Forma C - JSON / dict:")
    print(f"    {json.dumps(ast.dicc(), ensure_ascii=False)}")
    try:
        print(f"\n  Evaluacion del AST: {ast.evaluar(variables)}")
    except ValueError as ex:
        print(f"\n  Evaluacion del AST: ERROR semantico: {ex}")

    # ---- 3. Comparacion Parse Tree vs AST (diapo 14) ----
    print("\n[3] Parse Tree vs. AST (diapositiva 14):")
    print("  Parse Tree: representa TODAS las reglas, conserva no terminales")
    print("              (E, T, F) y detalles sintacticos. Esta ligado a la gramatica.")
    print("  AST       : representacion compacta, elimina simbolos innecesarios,")
    print("              destaca operadores y operandos. Facilita analisis posterior.")

    # ---- 4. Por que importa: AST correcto vs incorrecto ----
    print("\n[4] Comprobacion extra: agrupacion correcta vs incorrecta:")
    if (ast.valor == "+" and ast.der is not None and ast.der.valor == "*"):
        x, y, z = ast.izq.tupla(), ast.der.izq.tupla(), ast.der.der.tupla()
        incorrecto = Nodo("*", Nodo("+", ast.izq, ast.der.izq), ast.der.der)
        print(f"  Correcto   + ({x}, *({y},{z})) = {ast.evaluar(variables)}  <- respeta precedencia (* gana)")
        print(f"  Incorrecto * (+({x},{y}),{z}) = {incorrecto.evaluar(variables)}  <- ignora precedencia")
        print("  El Parse Tree de esta gramatica SOLO permite la forma correcta,")
        print("  por eso la gramatica por niveles elimina la ambiguedad.")
    else:
        print("  (Esta comparacion aplica a entradas de forma x + (y * z),")
        print(f"   como 3 + 4 * 5. La entrada actual dio: {ast.tupla()})")
    print()
    return True


def procesar_archivo(ruta):
    print(f"### Tarea #2 - Parse Tree vs AST | archivo: {ruta} ###\n")
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
            analizar("3 + 4 * 5")


if __name__ == "__main__":
    main()
