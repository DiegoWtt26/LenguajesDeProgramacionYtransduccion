# Tarea #2 — Parse Tree vs AST (diapos 12 y 13)

## Integrantes

- Camilo Bernal
- Diego Moreno
- Yeisson Rincón

Gramática por niveles (`Expr12.g4`):
`E -> E + T | T`, `T -> T * F | F`, `F -> id | num | (E)`.

El objetivo es mostrar la diferencia entre el Parse Tree completo y el AST reducido.

## Salida de `main.py` por cada línea
1. Estado sintáctico: ACEPTADA o RECHAZADA.
2. Parse Tree completo, con todos los niveles `E, T, F` (diapo 12).
3. AST con solo los operadores y operandos, presentado en tres formas:
   - dibujo en ASCII
   - tupla anidada, por ejemplo `('+', '3', ('*', '4', '5'))`
   - objeto JSON
   - además del valor evaluado (los identificadores reciben valor con la sintaxis `| a=2 b=3`)
4. Comparación punto por punto entre Parse Tree y AST (diapo 14).
5. Verificación del árbol correcto `+(3,*(4,5)) = 23` frente al árbol incorrecto `*(+(3,4),5) = 35`.

## Archivos
- `Expr12.g4`, `casos.txt`, `main.py`, archivos generados (`Expr12*.py`), `generar.sh`
- `Expr12LabLexer.g4`, `Expr12LabParser.g4` — versión adaptada para lab.antlr.org (regla inicial: `prog`)

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
cd "Tarea #2"
python3 main.py casos.txt
python3 main.py "3 + 4 * 5"
python3 main.py "a + b * c | a=2 b=3 c=4"
python3 main.py
```

Si no se indica ningún argumento, el programa utiliza el archivo `casos.txt`. En ese archivo el símbolo `#` marca un comentario y cada caso sigue el formato `expresion [| var=valor]`.

## Extra: derivaciones por izquierda y por derecha (`derivaciones.py`)

Este script complementa a `main.py`. Muestra las secuencias de formas sentenciales por la izquierda y por la derecha usando la gramática de la diapo 11, con el mismo parser ya generado.

```bash
cd "Tarea #2"
python3 derivaciones.py "3 + 4 * 5"
python3 derivaciones.py "3 + 4 * 5" "a + b * c" "(3 + 4) * 5"
```

Las dos secuencias terminan en la misma cadena de terminales; lo único que cambia es el orden en que se expanden los no terminales, no el árbol resultante. Esto confirma que la gramática no es ambigua.

## Regeneración del parser

```bash
chmod +x generar.sh
./generar.sh
```
