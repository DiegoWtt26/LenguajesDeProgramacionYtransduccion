# Tarea #3 — Diapositiva 15 TAL CUAL (gramática ambigua) (Linux)

Gramática del PDF tal cual en ANTLR (`ExprAmb.g4`):
`E -> E + E | E * E | num`. Sin paréntesis, sin precedencia.

## Qué hace `main.py` con cada línea del `.txt`
1. **Estado:** ACEPTADA / RECHAZADA + evaluación.
2. **Parseo tal cual** (`ExprAmb.g4`, `+` primero): `2+3*4` agrupa `(2+3)*4 = 20`.
3. **Detección exacta**: repite con `LL_EXACT_AMBIG_DETECTION` +
   `DiagnosticErrorListener`. Si ANTLR emite `reportAmbiguity`, queda
   comprobado (el warning/error ES el resultado esperado).
4. **Prueba definitiva** (`ExprAmbInv.g4`, orden invertido `*` primero):
   el MISMO input agrupa `2+(3*4) = 14`. Que el árbol dependa del orden
   arbitrario de las reglas demuestra que la gramática **es ambigua**.
5. **Dos interpretaciones** (diapos 16–17): `(2+3)*4 = 20` vs `2+(3*4) = 14`.

## Archivos
- `ExprAmb.g4` (tal cual) + `ExprAmbInv.g4` (orden invertido para probar)
- `casos.txt` — `2+3*4`, `2*3+4`, `42` (ACEPTADAS) + `2+*3`, `a+b` (RECHAZADAS: sin `num`)
- `main.py` — lee el `.txt`, dice ACEPTADA/RECHAZADA y evalúa cada una
- Parsers generados (`ExprAmb*.py`, `ExprAmbInv*.py`), `generar.sh`

## Versión para lab.antlr.org
- `ExprAmbLabLexer.g4` (Lexer, sin paréntesis) + `ExprAmbLabParser.g4` (Parser),
  Start rule: `prog`. Para ver el OTRO árbol, usa `ExprAmbInvLabParser.g4`.

## Requisitos (Linux)

```bash
python3 --version   # >= 3.10
pip install antlr4-python3-runtime==4.13.2
```

Con entorno virtual (recomendado):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install antlr4-python3-runtime==4.13.2
```

## Ejecución (Linux)

```bash
cd "Tarea #3"
python3 main.py casos.txt
python3 main.py "2 + 3 * 4"
python3 main.py
```

Sin argumentos usa `casos.txt`.

## Regenerar el parser

```bash
chmod +x generar.sh
./generar.sh
```
