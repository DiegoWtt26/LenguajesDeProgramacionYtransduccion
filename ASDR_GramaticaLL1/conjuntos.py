import os
import sys

EPS = "ε"
FIN = "$"


def leer_gramatica(ruta):
    reglas = []
    with open(ruta, encoding="utf-8") as f:
        for n, linea in enumerate(f, 1):
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            if "->" not in linea:
                print(f"Error en la línea {n} de la gramática: falta '->'")
                sys.exit(1)
            izquierda, derecha = linea.split("->", 1)
            simbolos = derecha.split()
            reglas.append((izquierda.strip(), simbolos if simbolos else [EPS]))

    no_terminales = []
    for A, _ in reglas:
        if A not in no_terminales:
            no_terminales.append(A)

    terminales = []
    for _, prod in reglas:
        for s in prod:
            if s not in no_terminales and s != EPS and s not in terminales:
                terminales.append(s)
    if FIN in terminales:
        terminales.remove(FIN)
    terminales.append(FIN)

    return reglas, no_terminales, terminales


def primeros_de(secuencia, primeros):
    resultado = set()
    for s in secuencia:
        if s == EPS:
            continue
        if s not in primeros:
            resultado.add(s)
            return resultado
        resultado |= primeros[s] - {EPS}
        if EPS not in primeros[s]:
            return resultado
    resultado.add(EPS)
    return resultado


def calcular_primeros(reglas, no_terminales):
    primeros = {A: set() for A in no_terminales}
    cambio = True
    while cambio:
        cambio = False
        for A, prod in reglas:
            nuevos = primeros_de(prod, primeros)
            if not nuevos <= primeros[A]:
                primeros[A] |= nuevos
                cambio = True
    return primeros


def calcular_siguientes(reglas, no_terminales, primeros):
    siguientes = {A: set() for A in no_terminales}
    siguientes[no_terminales[0]].add(FIN)
    cambio = True
    while cambio:
        cambio = False
        for A, prod in reglas:
            for i, B in enumerate(prod):
                if B not in siguientes:
                    continue
                resto = primeros_de(prod[i + 1:], primeros)
                nuevos = resto - {EPS}
                if EPS in resto:
                    nuevos |= siguientes[A]
                if not nuevos <= siguientes[B]:
                    siguientes[B] |= nuevos
                    cambio = True
    return siguientes


def calcular_prediccion(reglas, primeros, siguientes):
    prediccion = []
    for A, prod in reglas:
        prim = primeros_de(prod, primeros)
        pred = prim - {EPS}
        if EPS in prim:
            pred |= siguientes[A]
        prediccion.append(pred)
    return prediccion


def main():
    ruta = sys.argv[1] if len(sys.argv) > 1 else "gramatica.txt"
    if not os.path.isfile(ruta):
        print(f"Error: no existe el archivo '{ruta}'")
        sys.exit(1)

    reglas, no_terminales, terminales = leer_gramatica(ruta)
    if not reglas:
        print(f"Error: '{ruta}' no tiene producciones")
        sys.exit(1)

    primeros = calcular_primeros(reglas, no_terminales)
    siguientes = calcular_siguientes(reglas, no_terminales, primeros)
    prediccion = calcular_prediccion(reglas, primeros, siguientes)

    def conjunto(c):
        return "{ " + ", ".join(t for t in terminales + [EPS] if t in c) + " }"

    print(f"Gramática: {ruta}")
    print(f"Símbolo inicial: {no_terminales[0]}")

    print("\n===== CONJUNTO DE PRIMEROS =====")
    for A in no_terminales:
        print(f"PRIMEROS({A}) = {conjunto(primeros[A])}")

    print("\n===== CONJUNTO DE SIGUIENTES =====")
    for A in no_terminales:
        print(f"SIGUIENTES({A}) = {conjunto(siguientes[A])}")

    print("\n===== CONJUNTO DE PREDICCIÓN =====")
    for n, ((A, prod), pred) in enumerate(zip(reglas, prediccion), 1):
        print(f"{n:>2}. PRED({A} → {' '.join(prod)}) = {conjunto(pred)}")

    print("\n===== VERIFICACIÓN LL(1) =====")
    es_ll1 = True
    for A in no_terminales:
        indices = [i for i, (X, _) in enumerate(reglas) if X == A]
        if len(indices) < 2:
            continue
        comun = set()
        for a in range(len(indices)):
            for b in range(a + 1, len(indices)):
                comun |= prediccion[indices[a]] & prediccion[indices[b]]
        if comun:
            es_ll1 = False
            print(f"{A:<10} conflicto en {conjunto(comun)}")
        else:
            print(f"{A:<10} sin conflictos")
    print("Resultado:", "gramática LL(1)" if es_ll1 else "no es LL(1)")


if __name__ == "__main__":
    main()
