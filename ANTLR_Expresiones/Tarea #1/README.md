# Tarea #1 — Diapositiva 11 TAL CUAL (Linux)

Gramática del PDF tal cual en ANTLR (`Expr11.g4`):

```
E -> E + T | T
T -> T * F | F
F -> id | num | (E)
```

Solo `+` y `*`. Sin `-`.

## Archivos
- `Expr11.g4` — gramática ANTLR TAL CUAL (`e`, `t`, `f` + `prog`)
- `casos.txt` — casos de prueba, uno por línea. Formato `expresion [| var=valor]`
- `main.py` — lee el `.txt`, dice ACEPTADA/RECHAZADA y evalúa cada una
- `Expr11Lexer.py`, `Expr11Parser.py`, `Expr11Visitor.py`, `Expr11Listener.py` — generados con ANTLR 4.13.2
- `Expr11LabLexer.g4`, `Expr11LabParser.g4` — versión para lab.antlr.org (Start rule: `prog`)
- `generar.sh` — regenera el parser si se modifica la gramática (requiere Java + jar ANTLR)

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
cd "Tarea #1"
python3 main.py casos.txt
python3 main.py "2 + 3 * 4"
python3 main.py "a + b * c | a=2 b=3 c=4"
python3 main.py
```

Sin argumentos usa `casos.txt` por defecto.

## Regenerar el parser

```bash
chmod +x generar.sh
./generar.sh
```

Busca el jar en `$ANTLR_JAR` o `/tmp/antlr-4.13.2-complete.jar`. Descarga:

```bash
curl -L -o /tmp/antlr-4.13.2-complete.jar https://www.antlr.org/download/antlr-4.13.2-complete.jar
```

## Resultado esperado con `casos.txt`
- ACEPTADA: `2 + 3 * 4 = 14`, `2 + 3 * (4 + 5) = 29`, `a + b * c = 14`, `(2+3)*4 = 20`, `42`
- RECHAZADA: `2 + 3 - 4`, `2 + 3 * (4 - 5)` (usan `-`, que no existe en la gramática tal cual), `2 + * 3` (sintaxis inválida)
