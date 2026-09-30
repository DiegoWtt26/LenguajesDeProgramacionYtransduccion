import os
import sys
import threading

from lexico import ErrorLexico, todos_los_tokens
from parser import ErrorSintactico, Parser, mostrar_arbol
from semantico import AnalizadorSemantico, formato


def titulo(texto):
    print("\n" + "=" * 60)
    print(texto)
    print("=" * 60)


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 main.py <archivo_de_entrada>")
        return

    ruta = sys.argv[1]
    if not os.path.isfile(ruta):
        print(f"Error: no existe el archivo '{ruta}'")
        return

    with open(ruta, encoding="utf-8") as f:
        texto = f.read()

    titulo(f"ARCHIVO DE ENTRADA: {ruta}")
    for n, linea in enumerate(texto.splitlines(), 1):
        print(f"{n:>3} | {linea}")

    titulo("FASE 1: ANÁLISIS LÉXICO")
    try:
        tokens = todos_los_tokens(texto)
    except ErrorLexico as error:
        print(error)
        return
    print(f"{'TOKEN':<8}{'LEXEMA':<12}{'LÍNEA':<8}{'COLUMNA'}")
    print("-" * 36)
    for t in tokens:
        print(f"{t.tipo:<8}{t.lexema:<12}{t.linea:<8}{t.columna}")
    print("\nSin errores léxicos")

    titulo("FASE 2: ANÁLISIS SINTÁCTICO")
    try:
        sentencias = Parser(texto).inicio()
    except ErrorSintactico as error:
        print(error)
        return
    for sentencia in sentencias:
        mostrar_arbol(sentencia)
        print()
    print("Sin errores sintácticos")

    titulo("FASE 3: ANÁLISIS SEMÁNTICO")
    semantico = AnalizadorSemantico()
    semantico.ejecutar(sentencias)
    if semantico.errores:
        print()
        for error in semantico.errores:
            print(error)
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
    else:
        print("Programa ejecutado correctamente.")


if __name__ == "__main__":
    sys.setrecursionlimit(200000)
    threading.stack_size(256 * 1024 * 1024)
    hilo = threading.Thread(target=main)
    hilo.start()
    hilo.join()
