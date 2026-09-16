#!/usr/bin/env python3
# ============================================================
# Tarea #3 - Diapositiva 15 TAL CUAL: comprobar AMBIGUEDAD
# Gramatica: E -> E + E | E * E | num
#
# Uso (Linux):
#   python3 main.py casos.txt         (lee un .txt, uno por linea)
#   python3 main.py "2 + 3 * 4"
#   python3 main.py                   (usa casos.txt por defecto)
#
# Cada caso dice: ACEPTADA / RECHAZADA + evaluacion de cada arbol.
# Si el MISMO input da DOS arboles distintos (20 vs 14) => ES AMBIGUA.
#
# Requisito: pip3 install antlr4-python3-runtime==4.13.2
# Regenerar (solo si se modifica un .g4): ./generar.sh
# ============================================================
import os
import sys
from antlr4 import CommonTokenStream, InputStream
from antlr4.tree.Trees import Trees
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.DiagnosticErrorListener import DiagnosticErrorListener
from antlr4.atn.PredictionMode import PredictionMode

from ExprAmbLexer import ExprAmbLexer
from ExprAmbParser import ExprAmbParser
from ExprAmbVisitor import ExprAmbVisitor
from ExprAmbInvLexer import ExprAmbInvLexer
from ExprAmbInvParser import ExprAmbInvParser
from ExprAmbInvVisitor import ExprAmbInvVisitor


class ContadorErrores(ErrorListener):
    """Cuenta errores de sintaxis sin imprimir (evita mensajes duplicados)."""
    def __init__(self):
        self.n = 0

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.n += 1


class DetectorAmbiguedad(DiagnosticErrorListener):
    """DiagnosticErrorListener que SI muestra los reportAmbiguity."""
    def __init__(self):
        super().__init__(exactOnly=False)
        self.detectada = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if "reportAmbiguity" in msg or "ambigu" in msg.lower():
            self.detectada = True
        print(f"    [ANTLR] {msg}")


class EvalAmb(ExprAmbVisitor):
    def visitProg(self, ctx):
        return self.visit(ctx.expr())

    def visitSuma(self, ctx):
        return self.visit(ctx.expr(0)) + self.visit(ctx.expr(1))

    def visitMult(self, ctx):
        return self.visit(ctx.expr(0)) * self.visit(ctx.expr(1))

    def visitNum(self, ctx):
        return int(ctx.NUM().getText())


class EvalAmbInv(ExprAmbInvVisitor):
    def visitProg(self, ctx):
        return self.visit(ctx.expr())

    def visitSuma(self, ctx):
        return self.visit(ctx.expr(0)) + self.visit(ctx.expr(1))

    def visitMult(self, ctx):
        return self.visit(ctx.expr(0)) * self.visit(ctx.expr(1))

    def visitNum(self, ctx):
        return int(ctx.NUM().getText())


def parsear(parser_cls, lexer_cls, texto, oyentes):
    err_lex = ContadorErrores()
    lexer = lexer_cls(InputStream(texto))
    lexer.removeErrorListeners()
    lexer.addErrorListener(err_lex)
    parser = parser_cls(CommonTokenStream(lexer))
    parser.removeErrorListeners()
    for oyente in oyentes:
        parser.addErrorListener(oyente)
    tree = parser.prog()
    # Suma errores de lexer a cada oyente contador para que '(' o 'a' => RECHAZADA
    for oyente in oyentes:
        if isinstance(oyente, ContadorErrores):
            oyente.n += err_lex.n
    return parser, tree


def analizar(texto, num=None):
    etiqueta = f"[{num}] " if num is not None else ""
    print("=" * 64)
    print(f"{etiqueta}ENTRADA: {texto}")
    print("Gramatica: E -> E + E | E * E | num  (diapo 15, AMBIGUA TAL CUAL)")
    print("=" * 64)

    # ---- [1] Gramatica tal cual: '+' primero ----
    err1 = ContadorErrores()
    p1, t1 = parsear(ExprAmbParser, ExprAmbLexer, texto, [err1])
    arbol1 = Trees.toStringTree(t1, None, p1)
    val1 = EvalAmb().visit(t1) if err1.n == 0 else None

    # ---- [3] Orden invertido: '*' primero (se parsea ya para saber estado) ----
    err3 = ContadorErrores()
    p3, t3 = parsear(ExprAmbInvParser, ExprAmbInvLexer, texto, [err3])
    arbol3 = Trees.toStringTree(t3, None, p3)
    val3 = EvalAmbInv().visit(t3) if err3.n == 0 else None

    if err1.n > 0 or err3.n > 0:
        print("Estado     : RECHAZADA (error de sintaxis)")
        print("Evaluacion : -- (no se evalua lo rechazado)")
        print("Ambiguedad : -- (solo se analiza lo ACEPTADO)\n")
        return False

    print("Estado     : ACEPTADA")
    print("\n[1] ExprAmb.g4  (orden: E+E primero, E*E segundo):")
    print(f"    {arbol1}")
    print(f"    => valor = {val1}")

    # ---- [2] Deteccion exacta de ambiguedad ----
    print("\n[2] Deteccion exacta (LL_EXACT_AMBIG_DETECTION + diagnostico):")
    print("    >>> salida de ANTLR >>>")
    p2 = ExprAmbParser(CommonTokenStream(ExprAmbLexer(InputStream(texto))))
    p2.removeErrorListeners()
    detector = DetectorAmbiguedad()
    p2.addErrorListener(detector)
    p2._interp.predictionMode = PredictionMode.LL_EXACT_AMBIG_DETECTION
    p2.prog()  # el parseo dispara los reportes de diagnostico
    print("    <<< fin salida ANTLR <<<")
    if detector.detectada:
        print("    RESULTADO: ANTLR emitio reportAmbiguity => AMBIGUA (comprobado).")
    else:
        print("    NOTA: ANTLR4 asigna precedencia implicita por ORDEN en reglas")
        print("    recursivas a izquierda, asi que resuelve en silencio sin emitir")
        print("    reportAmbiguity. La comprobacion definitiva esta en [3].")
        print("    (El warning/error, si aparece, ES el resultado esperado.)")

    print("\n[3] ExprAmbInv.g4 (orden INVERTIDO: E*E primero, E+E segundo):")
    print(f"    {arbol3}")
    print(f"    => valor = {val3}")
    print()

    if " ".join(arbol1.split()) != " ".join(arbol3.split()):
        print("    PRUEBA: el mismo input produce DOS arboles distintos solo por")
        print("    cambiar el orden de las reglas. Si la gramatica fuera")
        print("    determinista, el orden no importaria. => ES AMBIGUA. COMPROBADO.")
        print(f"    Evaluacion: {val1} vs {val3} (diapos 16-17: 20 vs 14).")
    else:
        print("    NOTA: ambos ordenes dan el MISMO arbol para esta entrada")
        print("    (un solo operando: no hay dos agrupaciones posibles).")
        print("    La ambiguedad se observa con '2 + 3 * 4' sin parentesis:")
        print("    dos arboles posibles (ver resumen final).")

    # ---- [4] Las dos interpretaciones (diapos 16-17) ----
    print("\n[4] Las dos interpretaciones posibles (diapositivas 16-17):")
    print("""
      Interpretacion A:  (2 + 3) * 4        Interpretacion B:  2 + (3 * 4)

              *                                   +
            +   4                               2   *
           2 3                                     3 4

          = 5 * 4 = 20                          = 2 + 12 = 14
    """)
    print("  Conclusion (diapo 17): la gramatica debe fijar precedencia")
    print("  (* mayor que +) y asociatividad para quedar determinista,")
    print("  p. ej. con niveles E -> E + T | T,  T -> T * F | F.")
    print()
    return True


def procesar_archivo(ruta):
    print(f"### Tarea #3 - Ambiguedad TAL CUAL | archivo: {ruta} ###\n")
    ok = total = 0
    with open(ruta, encoding="utf-8") as f:
        n = 0
        for cruda in f:
            linea = cruda.strip()
            if not linea or linea.startswith("#"):
                continue
            n += 1
            total += 1
            if analizar(linea, n):
                ok += 1
    print(f"Resumen: {ok}/{total} ACEPTADAS, {total - ok}/{total} RECHAZADAS.")
    print("Lo ACEPTADO con dos operadores demuestra ambiguedad (dos arboles).")


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
            analizar("2 + 3 * 4")


if __name__ == "__main__":
    main()
