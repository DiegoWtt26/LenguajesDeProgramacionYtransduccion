# Tarea #2 — Parse Tree vs AST (diapos 12 y 13)

## Integrantes

- Camilo Bernal
- Diego Moreno
- Yeisson Rincón

Gramática por niveles (`Expr12.g4`):
`E -> E + T | T`, `T -> T * F | F`, `F -> id | num | (E)`.

Enfoque en la diferencia entre Parse Tree completo y AST reducido.

## Salida de `main.py` por línea
1. Estado: ACEPTADA / RECHAZADA.
2. Parse Tree completo, con `E, T, F` (diapo 12).
3. AST solo con operadores y operandos, en 3 formas:
   - dibujo ASCII
   - tupla tipo `('+', '3', ('*', '4', '5'))`
   - JSON
   - valor evaluado (identificadores con `| a=2 b=3`)
4. Comparación Parse vs AST (diapo 14).
5. Chequeo `+(3,*(4,5)) = 23` frente a `*(+(3,4),5) = 35`.

## Archivos
- `Expr12.g4`, `casos.txt`, `main.py`, generados (`Expr12*.py`), `generar.sh`
- `Expr12LabLexer.g4`, `Expr12LabParser.g4` — versión para lab.antlr.org (start rule: `prog`)

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
cd "Tarea #2"
python3 main.py casos.txt
python3 main.py "3 + 4 * 5"
python3 main.py "a + b * c | a=2 b=3 c=4"
python3 main.py
```

Sin argumentos, uso de `casos.txt`. En el txt, `#` comentario y formato `expresion [| var=valor]`.

## Extra: derivaciones izquierda y derecha (`derivaciones.py`)

Complemento de `main.py`. Secuencias de formas sentenciales por izquierda y por derecha con la gramática de la diapo 11. Uso del mismo parser generado.

```bash
cd "Tarea #2"
python3 derivaciones.py "3 + 4 * 5"
python3 derivaciones.py "3 + 4 * 5" "a + b * c" "(3 + 4) * 5"
```

Ambas secuencias terminan en la misma cadena de terminales. Cambio solo en el orden de expansión, no en el árbol. Gramática no ambigua.

## Regenerar

```bash
chmod +x generar.sh
./generar.sh
```
