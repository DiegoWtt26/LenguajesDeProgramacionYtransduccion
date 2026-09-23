# Tarea #3 — Gramática ambigua (diapo 15)

## Integrantes

- Camilo Bernal
- Diego Moreno
- Yeisson Rincón

Gramática del PDF llevada a ANTLR tal cual, sin paréntesis ni precedencia (`ExprAmb.g4`):
`E -> E + E | E * E | num`.

## Funcionamiento de `main.py`
1. Indica el estado (ACEPTADA o RECHAZADA) y muestra la evaluación.
2. Analiza con la gramática base (`ExprAmb.g4`, con el `+` en primer lugar): la entrada `2+3*4` se agrupa como `(2+3)*4 = 20`.
3. Repite el análisis con detección exacta de ambigüedad (`LL_EXACT_AMBIG_DETECTION` + `DiagnosticErrorListener`). Cuando ANTLR emite el aviso `reportAmbiguity`, la ambigüedad queda comprobada.
4. Analiza una vez más con la gramática invertida (`ExprAmbInv.g4`, con el `*` en primer lugar): la misma entrada se agrupa como `2+(3*4) = 14`. Que el árbol resultante dependa del orden de las reglas demuestra que la gramática es ambigua.
5. Muestra las dos interpretaciones (diapos 16-17): `(2+3)*4 = 20` frente a `2+(3*4) = 14`.

## Archivos
- `ExprAmb.g4` (gramática base) + `ExprAmbInv.g4` (gramática con el orden invertido, para la comparación)
- `casos.txt` — `2+3*4`, `2*3+4`, `42` como ACEPTADAS, y `2+*3`, `a+b` como RECHAZADAS (la gramática solo reconoce `num`)
- `main.py`, parsers generados y `generar.sh`

## Versión para lab.antlr.org
- `ExprAmbLabLexer.g4` + `ExprAmbLabParser.g4`, con regla inicial `prog`. El árbol alternativo se obtiene con `ExprAmbInvLabParser.g4`.

## Requisitos

```bash
python3 --version   # 3.10 o superior
pip install antlr4-python3-runtime==4.13.2
```

Con entorno virtual (opción recomendada):

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

Si no se indica ningún argumento, el programa utiliza el archivo `casos.txt`.

## Regeneración del parser

```bash
chmod +x generar.sh
./generar.sh
```
