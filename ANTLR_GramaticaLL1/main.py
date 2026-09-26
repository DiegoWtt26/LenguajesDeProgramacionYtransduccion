import os
import sys

from antlr4 import CommonTokenStream, FileStream

from generated.CalculadoraLexer import CalculadoraLexer
from generated.CalculadoraParser import CalculadoraParser
from errores import ListenerErroresLexicos, ListenerErroresSintacticos
from semantico import AnalizadorSemantico, formato


def titulo(texto):
    print("\n" + "=" * 60)
    print(texto)
    print("=" * 60)


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 main.py <archivo_de_entrada>")
        sys.exit(1)

    ruta = sys.argv[1]
    if not os.path.isfile(ruta):
        print(f"Error: no existe el archivo '{ruta}'")
        sys.exit(1)

    titulo(f"ARCHIVO DE ENTRADA: {ruta}")
    with open(ruta, encoding="utf-8") as f:
        for n, linea in enumerate(f.read().splitlines(), 1):
            print(f"{n:>3} | {linea}")

    entrada = FileStream(ruta, encoding="utf-8")

    # Fase 1: léxico
    titulo("FASE 1: ANÁLISIS LÉXICO")
    lexer = CalculadoraLexer(entrada)
    lexer.removeErrorListeners()
    errores_lex = ListenerErroresLexicos()
    lexer.addErrorListener(errores_lex)

    tokens = CommonTokenStream(lexer)
    tokens.fill()

    print(f"{'TOKEN':<12}{'LEXEMA':<12}{'LÍNEA':<8}{'COLUMNA'}")
    print("-" * 40)
    for tok in tokens.tokens:
        if tok.type == -1:
            nombre, lexema = "EOF", "$"
        else:
            nombre, lexema = CalculadoraLexer.symbolicNames[tok.type], tok.text
        print(f"{nombre:<12}{lexema:<12}{tok.line:<8}{tok.column + 1}")

    if errores_lex.errores:
        print()
        for err in errores_lex.errores:
            print(err)
    else:
        print("\nSin errores léxicos")

    # Fase 2: sintáctico
    titulo("FASE 2: ANÁLISIS SINTÁCTICO")
    parser = CalculadoraParser(tokens)
    parser.removeErrorListeners()
    errores_sin = ListenerErroresSintacticos()
    parser.addErrorListener(errores_sin)

    arbol = parser.inicio()

    if errores_sin.errores:
        for err in errores_sin.errores:
            print(err)
    else:
        print("Sin errores sintácticos")
        print("\nÁrbol sintáctico:")
        print(arbol.toStringTree(recog=parser))

    if errores_lex.errores or errores_sin.errores:
        titulo("RESULTADO")
        print("Hay errores léxicos o sintácticos; no se realiza el análisis semántico.")
        sys.exit(1)

    # Fase 3: semántico
    titulo("FASE 3: ANÁLISIS SEMÁNTICO")
    semantico = AnalizadorSemantico()
    semantico.visit(arbol)

    if semantico.errores:
        print()
        for err in semantico.errores:
            print(err)
    else:
        print("\nSin errores semánticos")

    titulo("TABLA DE SÍMBOLOS")
    print(f"{'VARIABLE':<12}{'VALOR'}")
    print("-" * 24)
    for nombre, valor in semantico.tabla_simbolos.items():
        print(f"{nombre:<12}{formato(valor)}")

    titulo("RESULTADO")
    if semantico.errores:
        print("El programa tiene errores semánticos.")
        sys.exit(1)
    print("Programa ejecutado correctamente.")


if __name__ == "__main__":
    main()
