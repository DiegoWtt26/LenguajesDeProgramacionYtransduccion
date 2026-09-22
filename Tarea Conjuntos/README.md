# Tarea Conjuntos — PRIMEROS, SIGUIENTES, PREDICCIÓN y tabla LL(1)

Referencia: PDF "Análisis sintáctico descendente", diapos 10–20 (cálculo),
24 (conflictos) y 28–29 (actividad guiada como modelo).

## Archivos (solo dentro de esta carpeta)

- `conjuntos.py` — motor genérico: anulables, PRIMEROS (diapos 11, 13),
  SIGUIENTES (diapo 15), PRED (diapo 17), tabla LL(1) (diapo 19) y conflictos (diapo 24).
- `main.py` — define las 2 gramáticas (ejercicios de las imágenes 1 y 2),
  imprime conjuntos, predicciones, tabla y veredicto LL(1), y verifica
  contra el cálculo a mano.

## Ejecución (Linux)

```bash
cd "Tarea Conjuntos"
python3 main.py      # ambos ejercicios
python3 main.py 1    # solo ejercicio 1
python3 main.py 2    # solo ejercicio 2
```

Requisitos (Linux): `python3 --version  # >= 3.10`. Sin dependencias externas
(solo biblioteca estándar, no hay `pip install`).

## Ejercicio 1 — `S → A uno B C | S dos ; A → B C D | A tres | ε ; ...`

Gramática completa en `main.py` (G1). Terminales: uno, dos, tres, cuatro, cinco, seis.

Anulables: {A, B, C, D}. S no es anulable (todas sus ramas traen uno/dos).

PRIMEROS:
- FIRST(D) = {seis, ε}
- FIRST(C) = {cinco, ε}
- FIRST(B) = {cuatro, seis, ε} (D anulable → entra cuatro)
- FIRST(A) = {tres, cuatro, cinco, seis, ε}
- FIRST(S) = {uno, tres, cuatro, cinco, seis} (el dos de S → S dos NUNCA es primero: S no es anulable, asi que FIRST(S dos) = FIRST(S))

SIGUIENTES (inicial $ ∈ FOLLOW(S); ε nunca va en SIGUIENTES):
- FOLLOW(S) = {$, dos} (por S → S dos)
- FOLLOW(A) = {uno, tres} (uno por S → A uno…; tres por A → A tres)
- FOLLOW(B) = {$, dos, uno, tres, cinco, seis}
- FOLLOW(C) = {$, dos, uno, tres, seis}
- FOLLOW(D) = {$, dos, uno, tres, cuatro, seis}

PRED (casos con ε suman FOLLOW, diapo 17):
- S → A uno B C: {uno, tres, cuatro, cinco, seis}
- S → S dos: {uno, tres, cuatro, cinco, seis} → choca con la anterior
- A → B C D: {uno, tres, cuatro, cinco, seis}
- A → A tres: {tres, cuatro, cinco, seis} → choca (recursión izquierda, diapo 24)
- A → ε: {uno, tres} → choca
- B → D cuatro C tres: {cuatro, seis}
- B → ε: {$, dos, uno, tres, cinco, seis} → choca en seis
- C → cinco D B: {cinco} | C → ε: {$, dos, uno, tres, seis} → disjuntas ✓
- D → seis: {seis} | D → ε: {$, dos, uno, tres, cuatro, seis} → choca en seis

Veredicto: NO es LL(1). Conflictos en S (uno, tres, cuatro, cinco, seis),
en A (M[A, uno], M[A, tres] triple, M[A, cuatro], M[A, cinco], M[A, seis]),
en M[B, seis] y en M[D, seis]. Además hay recursión izquierda
(S → S dos, A → A tres): antes de predecir habría que eliminarla (diapo 25).

## Ejercicio 2 — `S → A B uno ; A → dos B | ε ; B → C D | tres | ε ; ...`

Gramática completa en `main.py` (G2). Sin recursión izquierda, pero igual NO es LL(1).

Anulables: {A, B, D}. C y S no anulables.

PRIMEROS:
- FIRST(D) = {seis, ε}
- FIRST(C) = {cuatro, cinco}
- FIRST(B) = {tres, cuatro, cinco, ε}
- FIRST(A) = {dos, ε}
- FIRST(S) = {uno, dos, tres, cuatro, cinco} (A y B anulables → entra uno; seis no entra porque C no es anulable)

SIGUIENTES ($ solo queda en S, porque el uno final de S → A B uno bloquea la herencia):
- FOLLOW(S) = {$}
- FOLLOW(A) = FOLLOW(B) = FOLLOW(C) = FOLLOW(D) = {uno, tres, cuatro, cinco, seis}
  (A, B, C, D se heredan en ciclo por B → C D y C → cuatro A B).

PRED:
- S → A B uno: {uno, dos, tres, cuatro, cinco}
- A → dos B: {dos} | A → ε: {uno, tres, cuatro, cinco, seis} → disjuntas ✓
- B → C D: {cuatro, cinco} | B → tres: {tres} | B → ε: {uno, tres, cuatro, cinco, seis} → choca en tres, cuatro, cinco
- C → cuatro A B: {cuatro} | C → cinco: {cinco} → disjuntas ✓
- D → seis: {seis} | D → ε: {uno, tres, cuatro, cinco, seis} → choca en seis

Veredicto: NO es LL(1). Conflictos en M[B, tres], M[B, cuatro], M[B, cinco]
y M[D, seis]. La lección: quitar la recursión izquierda no basta; la anulabilidad
en ciclo (A↔B↔C) infla los FOLLOW y rompe la disyunción (diapo 24).

## Errores evitados (diapo 30)

- ε nunca en SIGUIENTES (el código lo blinda con discard).
- $ no se confunde con ε; $ solo nace en FOLLOW(S).
- FIRST(XY) con X anulable incorpora FIRST(Y) (no solo FIRST(X)).
- FOLLOW(A) solo se propaga si β es anulable/vacía.
- El veredicto LL(1) compara TODAS las alternativas, no una.
