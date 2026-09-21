#!/usr/bin/env python3
# ============================================================
# Tarea Analisis de Precedencia y Asociatividad (Linux)
# 4 gramaticas, mismo lenguaje (+ - * / parentesis, NUM):
#   G1 PrecLeft  : izquierda + precedencia CORRECTA  (*/ > +-)
#   G2 PrecRight : derecha   + precedencia CORRECTA  (*/ > +-)
#   G3 PrecInv   : izquierda + precedencia INVERTIDA (+- > */)
#   G4 PrecFlat  : sin niveles, todo a la izquierda (sin precedencia)
# Uso (Linux):
#   python3 main.py casos.txt       (combinado, una expresion por linea)
#   python3 main.py casos_g1.txt   (G1: izquierda + correcta)
#   python3 main.py casos_g2.txt   (G2: derecha + correcta)
#   python3 main.py casos_g3.txt   (G3: izquierda + invertida)
#   python3 main.py casos_g4.txt   (G4: plana)
#   python3 main.py "4 - 3 - 2"
#   python3 main.py                 (usa casos.txt por defecto)
# Requisito: pip3 install antlr4-python3-runtime==4.13.2
# Regenerar (solo si se modifica un .g4): ./generar.sh
# ============================================================
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "generado"))
from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener

from PrecLeftLexer import PrecLeftLexer
from PrecLeftParser import PrecLeftParser
from PrecLeftVisitor import PrecLeftVisitor
from PrecRightLexer import PrecRightLexer
from PrecRightParser import PrecRightParser
from PrecRightVisitor import PrecRightVisitor
from PrecInvLexer import PrecInvLexer
from PrecInvParser import PrecInvParser
from PrecInvVisitor import PrecInvVisitor
from PrecFlatLexer import PrecFlatLexer
from PrecFlatParser import PrecFlatParser
from PrecFlatVisitor import PrecFlatVisitor


class Silencio(ErrorListener):
    """Cuenta errores sin imprimir (el Estado lo reporta el programa)."""
    def __init__(self):
        self.n = 0

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.n += 1


def fmt(v):
    """1.0 -> '1', 6.666... -> '6.66667'. Evita el '-0'."""
    if isinstance(v, float):
        if v == 0:
            v = 0.0
        if v.is_integer():
            return str(int(v))
        return "%g" % v
    return str(v)


# ---------- AST compacto (diapo 13): solo operadores y operandos ----------
class Nodo:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

    def tupla(self):
        # Forma 1: tupla anidada  ('-', ('-', '4', '3'), '2')
        if self.izq is None and self.der is None:
            return self.valor
        return (self.valor, self.izq.tupla(), self.der.tupla())

    def dicc(self):
        # Forma 2: dict/JSON  {"op": "-", ...} / {"num": "4"}
        if self.izq is None and self.der is None:
            return {"num": self.valor}
        return {"op": self.valor, "izq": self.izq.dicc(), "der": self.der.dicc()}

    def evaluar(self):
        if self.izq is None:
            return int(self.valor)
        a, b = self.izq.evaluar(), self.der.evaluar()
        if self.valor == "+":
            return a + b
        if self.valor == "-":
            return a - b
        if self.valor == "*":
            return a * b
        return a / b  # '/' division real (float)

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


def _op(ctx):
    return ctx.getChild(1).getText()


class EvalLeft(PrecLeftVisitor):
    """G1: e:e op t | t ;  t:t op f | f (todo a la izquierda)."""
    def visitProg(self, ctx):
        return self.visit(ctx.e())

    def visitSumaResta(self, ctx):
        return Nodo(_op(ctx), self.visit(ctx.e()), self.visit(ctx.t()))

    def visitA_T(self, ctx):
        return self.visit(ctx.t())

    def visitMultDiv(self, ctx):
        return Nodo(_op(ctx), self.visit(ctx.t()), self.visit(ctx.f()))

    def visitA_F(self, ctx):
        return self.visit(ctx.f())

    def visitNum(self, ctx):
        return Nodo(ctx.NUM().getText())

    def visitParens(self, ctx):
        return self.visit(ctx.e())


class EvalRight(PrecRightVisitor):
    """G2: e:t op e | t ;  t:f op t | f (todo a la derecha)."""
    def visitProg(self, ctx):
        return self.visit(ctx.e())

    def visitSumaResta(self, ctx):
        return Nodo(_op(ctx), self.visit(ctx.t()), self.visit(ctx.e()))

    def visitA_T(self, ctx):
        return self.visit(ctx.t())

    def visitMultDiv(self, ctx):
        return Nodo(_op(ctx), self.visit(ctx.f()), self.visit(ctx.t()))

    def visitA_F(self, ctx):
        return self.visit(ctx.f())

    def visitNum(self, ctx):
        return Nodo(ctx.NUM().getText())

    def visitParens(self, ctx):
        return self.visit(ctx.e())


class EvalInv(PrecInvVisitor):
    """G3: niveles invertidos. e:e */ t | t ;  t:t +- f | f."""
    def visitProg(self, ctx):
        return self.visit(ctx.e())

    def visitMultDiv(self, ctx):
        return Nodo(_op(ctx), self.visit(ctx.e()), self.visit(ctx.t()))

    def visitA_T(self, ctx):
        return self.visit(ctx.t())

    def visitSumaResta(self, ctx):
        return Nodo(_op(ctx), self.visit(ctx.t()), self.visit(ctx.f()))

    def visitA_F(self, ctx):
        return self.visit(ctx.f())

    def visitNum(self, ctx):
        return Nodo(ctx.NUM().getText())

    def visitParens(self, ctx):
        return self.visit(ctx.e())


class EvalFlat(PrecFlatVisitor):
    """G4: expr: atom (op atom)* ; pliegue siempre por la izquierda."""
    def visitProg(self, ctx):
        return self.visit(ctx.expr())

    def visitExpr(self, ctx):
        atomos = ctx.atom()
        ops = ctx.op()
        nodo = self.visit(atomos[0])
        for i in range(len(ops)):
            nodo = Nodo(ops[i].getText(), nodo, self.visit(atomos[i + 1]))
        return nodo

    def visitAtom(self, ctx):
        if ctx.NUM() is not None:
            return Nodo(ctx.NUM().getText())
        return self.visit(ctx.expr())


GRAMATICAS = [
    ("G1", "izquierda + precedencia correcta (*/ > +-)",
     PrecLeftLexer, PrecLeftParser, EvalLeft),
    ("G2", "derecha + precedencia correcta (*/ > +-)",
     PrecRightLexer, PrecRightParser, EvalRight),
    ("G3", "izquierda + precedencia INVERTIDA (+- > */)",
     PrecInvLexer, PrecInvParser, EvalInv),
    ("G4", "sin niveles, todo a la izquierda (sin precedencia)",
     PrecFlatLexer, PrecFlatParser, EvalFlat),
]


def parsear(lexer_cls, parser_cls, texto):
    err_lex = Silencio()
    lexer = lexer_cls(InputStream(texto))
    lexer.removeErrorListeners()
    lexer.addErrorListener(err_lex)
    err_par = Silencio()
    parser = parser_cls(CommonTokenStream(lexer))
    parser.removeErrorListeners()
    parser.addErrorListener(err_par)
    tree = parser.prog()
    return tree, err_lex.n + err_par.n + parser.getNumberOfSyntaxErrors()


def analizar(texto, num=None):
    etiqueta = "[%d] " % num if num is not None else ""
    print("=" * 64)
    print("%sENTRADA: %s" % (etiqueta, texto))
    print("=" * 64)
    valores = {}
    for gid, desc, lex_cls, par_cls, vis_cls in GRAMATICAS:
        tree, n_err = parsear(lex_cls, par_cls, texto)
        if n_err > 0:
            print("\n%s (%s):" % (gid, desc))
            print("  Estado     : RECHAZADA (error de sintaxis)")
            print("  Evaluacion : -- (no se evalua lo rechazado)")
            valores[gid] = None
            continue
        ast = vis_cls().visit(tree)
        try:
            val = ast.evaluar()
        except ZeroDivisionError:
            print("\n%s (%s):" % (gid, desc))
            print("  Estado     : ACEPTADA")
            print("  Evaluacion : ERROR semantico: division por cero")
            valores[gid] = None
            continue
        valores[gid] = val
        print("\n%s (%s):" % (gid, desc))
        print("  Estado     : ACEPTADA")
        print("  AST ASCII  :")
        print("    %s" % ast.valor)
        hijos = [h for h in (ast.izq, ast.der) if h is not None]
        for i, h in enumerate(hijos):
            for linea in h.ascii("    ", i == len(hijos) - 1):
                print("   " + linea)
        print("  AST tupla  : %s" % (ast.tupla(),))
        print("  Evaluacion : %s" % fmt(val))

    # ---- comparativas (diapos 27-30) ----
    print("\nComparativa:")
    aceptadas = {g: valores[g] for g in valores if valores[g] is not None}
    if len(aceptadas) < 4:
        print("  (hay gramaticas que RECHAZAN: solo se compara lo ACEPTADO)")
    if "G1" in aceptadas and "G2" in aceptadas:
        if fmt(aceptadas["G1"]) == fmt(aceptadas["G2"]):
            print("  Asociatividad G1 vs G2: %s = %s (no se distingue aqui)" %
                  (fmt(aceptadas["G1"]), fmt(aceptadas["G2"])))
        else:
            print("  Asociatividad G1 vs G2: %s (izq) vs %s (der) => AGRUPAN DISTINTO" %
                  (fmt(aceptadas["G1"]), fmt(aceptadas["G2"])))
    if "G1" in aceptadas and "G3" in aceptadas and "G4" in aceptadas:
        if fmt(aceptadas["G1"]) == fmt(aceptadas["G3"]) == fmt(aceptadas["G4"]):
            print("  Precedencia G1=G3=G4=%s (misma agrupacion: sin mezcla de niveles)" %
                  fmt(aceptadas["G1"]))
        else:
            print("  Precedencia G1=%s (correcta) vs G3=%s (invertida) vs G4=%s (plana)" %
                  (fmt(aceptadas["G1"]), fmt(aceptadas["G3"]), fmt(aceptadas["G4"])))
    print()
    return valores


def procesar_archivo(ruta):
    print("### Analisis de Precedencia y Asociatividad | archivo: %s ###\n" % ruta)
    cuenta = {g: 0 for g, _, _, _, _ in GRAMATICAS}
    total = 0
    with open(ruta, encoding="utf-8") as f:
        n = 0
        for cruda in f:
            linea = cruda.strip()
            if not linea or linea.startswith("#"):
                continue
            n += 1
            total += 1
            for g, v in analizar(linea, n).items():
                if v is not None:
                    cuenta[g] += 1
    print("Resumen (casos con valor, por gramatica): " +
          ", ".join("%s %d/%d" % (g, cuenta[g], total) for g in cuenta) + ".")


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
                analizar(arg)
    else:
        if os.path.isfile(defecto):
            procesar_archivo(defecto)
        else:
            analizar("4 - 3 - 2")


if __name__ == "__main__":
    main()
