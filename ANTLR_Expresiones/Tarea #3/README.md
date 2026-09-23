# Tarea #3 — Gramática ambigua (diapo 15)

Gramática del PDF, sin paréntesis ni precedencia (`ExprAmb.g4`):
`E -> E + E | E * E | num`.

## Funcionamiento de `main.py`
1. Estado ACEPTADA / RECHAZADA + evaluación.
2. Parseo base (`ExprAmb.g4`, `+` primero): `2+3*4` como `(2+3)*4 = 20`.
3. Detección exacta con `LL_EXACT_AMBIG_DETECTION` + `DiagnosticErrorListener`. El `reportAmbiguity` de ANTLR como confirmación.
4. Segundo parseo (`ExprAmbInv.g4`, `*` primero): mismo input como `2+(3*4) = 14`. Dependencia del orden de reglas = ambigüedad.
5. Dos lecturas (diapos 16-17): `(2+3)*4 = 20` vs `2+(3*4) = 14`.

## Archivos
- `ExprAmb.g4` (base) + `ExprAmbInv.g4` (orden invertido)
- `casos.txt` — `2+3*4`, `2*3+4`, `42` (ACEPTADAS) + `2+*3`, `a+b` (RECHAZADAS, solo `num`)
- `main.py`, parsers generados, `generar.sh`

## Versión lab.antlr.org
- `ExprAmbLabLexer.g4` + `ExprAmbLabParser.g4`, start rule: `prog`. Árbol alterno con `ExprAmbInvLabParser.g4`.

## Requisitos

```bash
python3 --version   # >= 3.10
pip install antlr4-python3-runtime==4.13.2
```

Con entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install antlr4-python3-runtime==4.13.2
```

## Ejecución

```bash
cd "Tarea #3"
python3 main.py casos.txt
python3 main.py "2 + 3 * 4"
python3 main.py
```

Sin argumentos, uso de `casos.txt`.

## Regenerar

```bash
chmod +x generar.sh
./generar.sh
```
