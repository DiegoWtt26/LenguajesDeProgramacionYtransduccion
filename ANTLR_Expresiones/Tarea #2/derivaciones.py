#!/usr/bin/env python3
# ============================================================
# Tarea #2 (extra) - Derivacion por la izquierda y por la derecha
#
# Complementa el AST/Parse Tree (main.py) con las derivaciones
# formales, por si "diferentes formas de AT" se referia a las
# derivaciones (izquierda/derecha) y no al AST.
#
# Usa el MISMO parser ya generado (Expr12Lexer/Expr12Parser) de
# la gramatica de la diapo 11/12:
#   E -> E + T | T ;  T -> T * F | F ;  F -> id | num | ( E )
#
# No inventa la derivacion a mano: recorre el parse tree que ya
# construyo ANTLR y en cada paso expande el no-terminal mas a la
# izquierda (o mas a la derecha), tal como se hace en papel.
#
# Uso (Linux):
#   python3 derivaciones.py "3 + 4 * 5"
#   python3 derivaciones.py            (usa "3 + 4 * 5" por defecto)
#
# Requisito: pip3 install antlr4-python3-runtime==4.13.2
# ============================================================
import sys

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Tree import TerminalNode

from Expr12Lexer import Expr12Lexer
from Expr12Parser import Expr12Parser


class Silencio(ErrorListener):
    """Evita que ANTLR imprima errores por stderr; los contamos nosotros."""
    def __init__(self):
        self.n = 0

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.n += 1


def parsear(texto):
    """Parsea 'texto' y devuelve la raiz de E (sin 'prog' ni EOF)."""
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
        return None, parser
    return tree.e(), parser


def simbolo(nodo, parser):
    """Texto a mostrar: E/T/F si es no-terminal, el texto literal si es terminal."""
    if isinstance(nodo, TerminalNode):
        return nodo.getText()
    return parser.ruleNames[nodo.getRuleIndex()].upper()


def forma_sentencial(forma, parser):
    return " ".join(simbolo(s, parser) for s in forma)


def derivar(raiz, parser, direccion="izquierda"):
    """
    Genera la secuencia de formas sentenciales de una derivacion por
    la izquierda o por la derecha, expandiendo en cada paso el
    no-terminal mas a la izquierda (o mas a la derecha) segun el
    parse tree que ya construyo ANTLR (no se inventa nada nuevo,
    solo se recorre en el orden correspondiente).
    """
    forma = [raiz]
    pasos = [forma_sentencial(forma, parser)]
    while any(not isinstance(s, TerminalNode) for s in forma):
        no_terminales = [i for i, s in enumerate(forma) if not isinstance(s, TerminalNode)]
        idx = no_terminales[0] if direccion == "izquierda" else no_terminales[-1]
        nodo = forma[idx]
        hijos = [nodo.getChild(i) for i in range(nodo.getChildCount())]
        forma = forma[:idx] + hijos + forma[idx + 1:]
        pasos.append(forma_sentencial(forma, parser))
    return pasos


def mostrar(texto):
    print("=" * 64)
    print(f"ENTRADA: {texto}")
    print("Gramatica (diapo 11/12): E -> E + T | T ; T -> T * F | F ; F -> id|num|(E)")
    print("=" * 64)
    raiz, parser = parsear(texto)
    if raiz is None:
        print("RECHAZADA (error de sintaxis)\n")
        return

    izq = derivar(raiz, parser, "izquierda")
    der = derivar(raiz, parser, "derecha")

    print("\n[Derivacion por la IZQUIERDA] (se expande el no-terminal mas a la izquierda):")
    for i, paso in enumerate(izq):
        print(f"  {i}: {paso}")

    print("\n[Derivacion por la DERECHA] (se expande el no-terminal mas a la derecha):")
    for i, paso in enumerate(der):
        print(f"  {i}: {paso}")

    print("\nConclusion:")
    print("  Son dos SECUENCIAS distintas de pasos (distinto orden de expansion),")
    print("  pero ambas terminan en la MISMA cadena de simbolos terminales y en")
    print("  el MISMO arbol de derivacion: la gramatica por niveles (E/T/F) NO")
    print("  es ambigua, solo hay un arbol posible; lo unico que cambia entre")
    print("  las dos derivaciones es el orden en que se van reemplazando los")
    print("  no-terminales, no el resultado final.")
    print()


def main():
    textos = sys.argv[1:] if len(sys.argv) > 1 else ["3 + 4 * 5"]
    for texto in textos:
        mostrar(texto)


if __name__ == "__main__":
    main()
