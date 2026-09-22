#!/usr/bin/env python3
"""Tarea Conjuntos — FIRST / FOLLOW / PREDICT / tabla LL(1) para las 2 gramaticas.

Uso (Linux):  python3 main.py        (corre ejercicio 1 y 2)
      python3 main.py 1      (solo ejercicio 1)
      python3 main.py 2      (solo ejercicio 2)

Metodo (PDF diapos 10-20): punto fijo para PRIMEROS y SIGUIENTES,
PRED(A->alfa) segun diapo 17, tabla segun diapo 19, conflicto segun diapo 24.
"""
import sys
from conjuntos import (
    EPS, END, calcular_nullable, calcular_first, calcular_follow,
    calcular_predict, construir_tabla, conflictos, fmt_conj, fmt_alt,
)

# ---- Ejercicio 1 (Image 1) ----
G1 = {
    "S": [["A", "uno", "B", "C"], ["S", "dos"]],
    "A": [["B", "C", "D"], ["A", "tres"], [EPS]],
    "B": [["D", "cuatro", "C", "tres"], [EPS]],
    "C": [["cinco", "D", "B"], [EPS]],
    "D": [["seis"], [EPS]],
}
# ---- Ejercicio 2 (Image 2) ----
G2 = {
    "S": [["A", "B", "uno"]],
    "A": [["dos", "B"], [EPS]],
    "B": [["C", "D"], ["tres"], [EPS]],
    "C": [["cuatro", "A", "B"], ["cinco"]],
    "D": [["seis"], [EPS]],
}

# Valores esperados (calculados a mano con las reglas del PDF; el programa los verifica).
ESP1_FIRST = {
    "S": {"uno", "tres", "cuatro", "cinco", "seis"},
    "A": {"tres", "cuatro", "cinco", "seis", EPS},
    "B": {"cuatro", "seis", EPS},
    "C": {"cinco", EPS},
    "D": {"seis", EPS},
}
ESP1_FOLLOW = {
    "S": {END, "dos"},
    "A": {"uno", "tres"},
    "B": {END, "dos", "uno", "tres", "cinco", "seis"},
    "C": {END, "dos", "uno", "tres", "seis"},
    "D": {END, "dos", "uno", "tres", "cuatro", "seis"},
}
ESP2_FIRST = {
    "S": {"uno", "dos", "tres", "cuatro", "cinco"},
    "A": {"dos", EPS},
    "B": {"tres", "cuatro", "cinco", EPS},
    "C": {"cuatro", "cinco"},
    "D": {"seis", EPS},
}
ESP2_FOLLOW = {
    "S": {END},
    "A": {"uno", "tres", "cuatro", "cinco", "seis"},
    "B": {"uno", "tres", "cuatro", "cinco", "seis"},
    "C": {"uno", "tres", "cuatro", "cinco", "seis"},
    "D": {"uno", "tres", "cuatro", "cinco", "seis"},
}


def analizar(nombre, gramatica, inicial, esp_first=None, esp_follow=None):
    print("=" * 70)
    print(nombre)
    print("=" * 70)
    for nt, alts in gramatica.items():
        for alt in alts:
            print(f"  {nt} -> {fmt_alt(alt)}")
    anul = calcular_nullable(gramatica)
    first = calcular_first(gramatica, anul)
    follow = calcular_follow(gramatica, first, anul, inicial)
    preds = calcular_predict(gramatica, first, follow)
    tabla = construir_tabla(gramatica, preds)
    conf = conflictos(tabla)

    print(f"\nAnulables: {fmt_conj(anul)}")
    print("\nPRIMEROS:")
    for nt in gramatica:
        print(f"  PRIMEROS({nt}) = {fmt_conj(first[nt])}")
    print("\nSIGUIENTES:")
    for nt in gramatica:
        print(f"  SIGUIENTES({nt}) = {fmt_conj(follow[nt])}")
    print("\nPREDICCION por produccion:")
    for nt, i, alt, fa, pred in preds:
        print(f"  {nt} -> {fmt_alt(alt):<18} FIRST={fmt_conj(fa):<32} PRED={fmt_conj(pred)}")

    # Tabla LL(1): columnas = terminales + $
    terms = sorted(
        {s for alts in gramatica.values() for alt in alts for s in alt
         if s not in gramatica and s != EPS} | {END}
    )
    print("\nTabla LL(1)  (. = error):")
    print("      " + "".join(f"{t:<14}" for t in terms))
    for nt in gramatica:
        fila = f"  {nt:<4}"
        for t in terms:
            c = tabla.get((nt, t), [])
            if not c:
                fila += f"{'.':<14}"
            elif len(c) == 1:
                fila += f"{nt}->{fmt_alt(gramatica[nt][c[0]])[:12]:<12}  "
            else:
                fila += f"{'CONFLICTO':<14}"
        print(fila)

    if conf:
        print("\nNO es LL(1). Conflictos (diapo 24: dos PRED se intersectan):")
        for (nt, t), idxs in sorted(conf.items()):
            alts = [f"{nt} -> {fmt_alt(gramatica[nt][i])}" for i in idxs]
            print(f"  M[{nt}, {t}]: " + "  |  ".join(alts))
    else:
        print("\nSI es LL(1): cada celda tiene maximo una produccion.")

    ok = True
    if esp_first:
        for nt, esp in esp_first.items():
            if first[nt] != esp:
                ok = False
                print(f"  [DIF] FIRST({nt}): calc={fmt_conj(first[nt])} esperado={fmt_conj(esp)}")
    if esp_follow:
        for nt, esp in esp_follow.items():
            if follow[nt] != esp:
                ok = False
                print(f"  [DIF] FOLLOW({nt}): calc={fmt_conj(follow[nt])} esperado={fmt_conj(esp)}")
    print(("\nVerificacion: OK (coincide con el calculo a mano).\n" if ok
           else "\nVerificacion: HAY DIFERENCIAS (revisar arriba).\n"))
    return {"first": first, "follow": follow, "conflictos": conf}


def main():
    args = sys.argv[1:]
    if not args:
        analizar("Ejercicio 1: S -> A uno B C | S dos ; ...", G1, "S", ESP1_FIRST, ESP1_FOLLOW)
        analizar("Ejercicio 2: S -> A B uno ; ...", G2, "S", ESP2_FIRST, ESP2_FOLLOW)
    elif args[0] == "1":
        analizar("Ejercicio 1", G1, "S", ESP1_FIRST, ESP1_FOLLOW)
    elif args[0] == "2":
        analizar("Ejercicio 2", G2, "S", ESP2_FIRST, ESP2_FOLLOW)
    else:
        print("Uso: python3 main.py [1|2]")


if __name__ == "__main__":
    main()
