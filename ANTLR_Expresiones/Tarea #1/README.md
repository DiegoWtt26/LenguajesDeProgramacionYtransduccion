# Tarea #1 — Diapo 11 tal cual

## Integrantes

- Camilo Bernal
- Diego Moreno
- Yeisson Rincón

Gramática de la diapo 11 llevada a ANTLR (`Expr11.g4`), sin ninguna modificación:

```
E -> E + T | T
T -> T * F | F
F -> id | num | (E)
```

La gramática solo reconoce los operadores `+` y `*`; el operador `-` no forma parte de ella.

## Archivos
- `Expr11.g4` — gramática con las reglas `e`, `t`, `f` y `prog`
- `casos.txt` — casos de prueba, uno por línea, con el formato `expresion [| var=valor]`
- `main.py` — lee el archivo de texto, indica ACEPTADA o RECHAZADA para cada línea y muestra su evaluación
- `Expr11Lexer.py`, `Expr11Parser.py`, `Expr11Visitor.py`, `Expr11Listener.py` — archivos producidos por ANTLR 4.13.2
- `Expr11LabLexer.g4`, `Expr11LabParser.g4` — versión adaptada para lab.antlr.org (regla inicial: `prog`)
- `generar.sh` — regenera el parser si se modifica la gramática (requiere Java y el jar de ANTLR)

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
cd "Tarea #1"
python3 main.py casos.txt
python3 main.py "2 + 3 * 4"
python3 main.py "a + b * c | a=2 b=3 c=4"
python3 main.py
```

Si no se indica ningún argumento, el programa utiliza el archivo `casos.txt` por defecto.

## Regeneración del parser

```bash
chmod +x generar.sh
./generar.sh
```

El script busca el archivo jar en la variable `$ANTLR_JAR` o en la ruta `/tmp/antlr-4.13.2-complete.jar`. Si no existe, se descarga con:

```bash
curl -L -o /tmp/antlr-4.13.2-complete.jar https://www.antlr.org/download/antlr-4.13.2-complete.jar
```

## Resultado esperado con `casos.txt`
- ACEPTADA: `2 + 3 * 4 = 14`, `2 + 3 * (4 + 5) = 29`, `a + b * c = 14`, `(2+3)*4 = 20`, `42`
- RECHAZADA: `2 + 3 - 4`, `2 + 3 * (4 - 5)` (usan el operador `-`, que no existe en esta gramática), `2 + * 3` (sintaxis inválida)
