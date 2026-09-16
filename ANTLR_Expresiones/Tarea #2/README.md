# Tarea #2 — Diapositivas 12 (Parse Tree) y 13 (AST) (Linux)

## Gramática
La misma de expresiones por niveles (`Expr12.g4`):
`E -> E + T | T`, `T -> T * F | F`, `F -> id | num | (E)`.

## Qué comprueba `main.py` con cada línea del `.txt`
1. **Estado:** ACEPTADA / RECHAZADA (sintaxis).
2. **Parse Tree (diapo 12):** estructura completa con `E, T, F`.
3. **AST (diapo 13):** compacto, solo operadores/operandos, en 3 formas:
   - **Forma A:** dibujo ASCII (`+` con hijos `3` y `*`, y `*` con `4`,`5`)
   - **Forma B:** tupla anidada `('+', '3', ('*', '4', '5'))`
   - **Forma C:** JSON `{"op": "+", "izq": ..., "der": ...}`
   - **Evaluación** del AST (con tabla `| a=2 b=3` si hay identificadores).
4. **Parse Tree vs AST** (diapo 14): comparación punto por punto.
5. **Comprobación extra:** AST correcto `+(3,*(4,5)) = 23` vs incorrecto `*(+(3,4),5) = 35`.

## Archivos
- `Expr12.g4`, `casos.txt`, `main.py`, parser generado (`Expr12*.py`), `generar.sh`
- `Expr12LabLexer.g4`, `Expr12LabParser.g4` — versión para lab.antlr.org (Start rule: `prog`)

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
cd "Tarea #2"
python3 main.py casos.txt
python3 main.py "3 + 4 * 5"
python3 main.py "a + b * c | a=2 b=3 c=4"
python3 main.py
```

Sin argumentos usa `casos.txt`. Formato del `.txt`: `expresion [| var=valor]`, `#` comentario.

## Regenerar el parser

```bash
chmod +x generar.sh
./generar.sh
```
