import re
import sys

EPS = "ε"
FIN = "$"


def leer_gramatica(ruta):
    with open(ruta, encoding="utf-8") as f:
        texto = f.read()

    texto = re.sub(r"/\*.*?\*/", "", texto, flags=re.DOTALL)
    texto = re.sub(r"//[^\n]*", "", texto)
    texto = re.sub(r"^\s*grammar\s+\w+\s*;", "", texto, flags=re.MULTILINE)

    reglas = re.findall(r"([A-Za-z_]\w*)\s*:((?:'[^']*'|[^;'])*);", texto)

    gramatica = {}
    literales = {}
    orden_terminales = []

    for nombre, cuerpo in reglas:
        cuerpo = cuerpo.strip()
        if nombre[0].isupper():
            if "-> skip" in cuerpo:
                continue
            orden_terminales.append(nombre)
            literal = re.fullmatch(r"'([^']*)'", cuerpo)
            if literal:
                literales[nombre] = literal.group(1)
        else:
            producciones = []
            for alternativa in cuerpo.split("|"):
                simbolos = alternativa.split()
                simbolos = [FIN if s == "EOF" else s for s in simbolos]
                producciones.append(simbolos if simbolos else [EPS])
            gramatica[nombre] = producciones

    return gramatica, literales, orden_terminales + [FIN]


def primeros_de(secuencia, primeros, gramatica):
    resultado = set()
    for simbolo in secuencia:
        if simbolo == EPS:
            continue
        if simbolo not in gramatica:
            resultado.add(simbolo)
            return resultado
        resultado |= primeros[simbolo] - {EPS}
        if EPS not in primeros[simbolo]:
            return resultado
    resultado.add(EPS)
    return resultado


def calcular_primeros(gramatica):
    primeros = {A: set() for A in gramatica}
    cambio = True
    while cambio:
        cambio = False
        for A, producciones in gramatica.items():
            for prod in producciones:
                nuevos = primeros_de(prod, primeros, gramatica)
                if not nuevos <= primeros[A]:
                    primeros[A] |= nuevos
                    cambio = True
    return primeros


def calcular_siguientes(gramatica, primeros, inicial):
    siguientes = {A: set() for A in gramatica}
    siguientes[inicial].add(FIN)
    cambio = True
    while cambio:
        cambio = False
        for A, producciones in gramatica.items():
            for prod in producciones:
                for i, B in enumerate(prod):
                    if B not in gramatica:
                        continue
                    resto = primeros_de(prod[i + 1:], primeros, gramatica)
                    nuevos = resto - {EPS}
                    if EPS in resto:
                        nuevos |= siguientes[A]
                    if not nuevos <= siguientes[B]:
                        siguientes[B] |= nuevos
                        cambio = True
    return siguientes


def calcular_prediccion(gramatica, primeros, siguientes):
    prediccion = []
    for A, producciones in gramatica.items():
        for prod in producciones:
            prim = primeros_de(prod, primeros, gramatica)
            pred = prim - {EPS}
            if EPS in prim:
                pred |= siguientes[A]
            prediccion.append((A, prod, pred))
    return prediccion


def buscar_conflictos(gramatica, prediccion):
    conflictos = []
    for A in gramatica:
        reglas = [(prod, pred) for (nt, prod, pred) in prediccion if nt == A]
        for i in range(len(reglas)):
            for j in range(i + 1, len(reglas)):
                comun = reglas[i][1] & reglas[j][1]
                if comun:
                    conflictos.append((A, reglas[i][0], reglas[j][0], comun))
    return conflictos


def main():
    ruta = sys.argv[1] if len(sys.argv) > 1 else "Calculadora.g4"
    gramatica, literales, orden = leer_gramatica(ruta)
    inicial = next(iter(gramatica))

    def mostrar(simbolo):
        return literales.get(simbolo, simbolo)

    def conjunto(c):
        return "{ " + ", ".join(mostrar(t) for t in orden + [EPS] if t in c) + " }"

    def regla(A, prod):
        return f"{A} → {' '.join(mostrar(s) for s in prod)}"

    primeros = calcular_primeros(gramatica)
    siguientes = calcular_siguientes(gramatica, primeros, inicial)
    prediccion = calcular_prediccion(gramatica, primeros, siguientes)
    conflictos = buscar_conflictos(gramatica, prediccion)

    print(f"Gramática leída de: {ruta}")
    print(f"Símbolo inicial: {inicial}")

    print("\n===== CONJUNTO DE PRIMEROS =====")
    for A in gramatica:
        print(f"PRIMEROS({A}) = {conjunto(primeros[A])}")

    print("\n===== CONJUNTO DE SIGUIENTES =====")
    for A in gramatica:
        print(f"SIGUIENTES({A}) = {conjunto(siguientes[A])}")

    print("\n===== CONJUNTO DE PREDICCIÓN =====")
    for n, (A, prod, pred) in enumerate(prediccion, 1):
        print(f"{n:>2}. PRED({regla(A, prod)}) = {conjunto(pred)}")

    print("\n===== VERIFICACIÓN LL(1) =====")
    for A, producciones in gramatica.items():
        if len(producciones) < 2:
            continue
        propios = [c for c in conflictos if c[0] == A]
        if propios:
            comun = set().union(*(c[3] for c in propios))
            print(f"{A:<10} conflicto en {conjunto(comun)}")
        else:
            print(f"{A:<10} sin conflictos")
    print("Resultado:", "no es LL(1)" if conflictos else "gramática LL(1)")

if __name__ == "__main__":
    main()
