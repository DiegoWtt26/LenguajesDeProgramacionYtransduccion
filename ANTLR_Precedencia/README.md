# Tarea — Análisis de Precedencia y Asociatividad (Linux)

Referencia: PDF de Análisis Sintáctico, diapos 27–31 (asociatividad y
precedencia), 30 (niveles gramaticales), 36 (gramática estilo ANTLR) y
38 (actividad 2 de diseño). Todo lo de aquí es para Linux (bash).

## Las 4 gramáticas

Mismo lenguaje en las 4 (`+ - * /`, paréntesis, `NUM`; división real):

| ID | Reglas clave | Asociatividad | Precedencia |
|----|--------------|---------------|-------------|
| G1 `PrecLeft.g4` | `e:e op t \| t` , `t:t op f \| f` | izquierda | correcta: `*/ > +-` (diapos 27, 30) |
| G2 `PrecRight.g4` | `e:t op e \| t` , `t:f op t \| f` | derecha (diapo 28: `E → T op E`) | correcta: `*/ > +-` |
| G3 `PrecInv.g4` | `e:e */ t \| t` , `t:t +- f \| f` | izquierda | INVERTIDA a propósito: `+- > */` |
| G4 `PrecFlat.g4` | `expr: atom (op atom)*` | izquierda | SIN niveles: todo se pliega de izquierda a derecha |

G1 es la gramática de referencia (la buena). G2 solo cambia la dirección
de la recursión; G3 intercambia los niveles; G4 elimina los niveles.

## Qué comprueba `main.py`

Por cada línea del `.txt`, corre las 4 gramáticas e imprime por cada una:
`Estado` (ACEPTADA / RECHAZADA), AST en ASCII (diapo 13), AST en tupla y
evaluación. Después imprime la comparativa:

- **Asociatividad G1 vs G2** (diapo 27): con `4 - 3 - 2`, G1 da
  `(4-3)-2 = -1` y G2 da `4-(3-2) = 3`. Distinto árbol, distinto valor.
- **Precedencia G1 vs G3 vs G4** (diapos 29–30): con `2 + 3 * 4`, G1 da
  `2+(3*4) = 14`, mientras G3 da `(2+3)*4 = 20` (nivel invertido) y G4 da
  `20` (sin niveles, de izquierda a derecha).
- Los paréntesis mandan en las 4: `(2+3)*4 = 20`, `2*(3+4) = 14`.

Tabla esperada con `casos.txt` (generalizado, 19 casos en 5 bloques):

| caso | G1 izq-ok | G2 der-ok | G3 invertida | G4 plana |
|------|-----------|-----------|--------------|----------|
| `4 - 3 - 2` | -1 | 3 | -1 | -1 |
| `8 / 4 / 2` | 1 | 4 | 1 | 1 |
| `10 - 2 + 3` | 11 | 5 | 11 | 11 |
| `2 + 3 + 4` | 9 | 9 | 9 | 9 |
| `2 * 3 * 4` | 24 | 24 | 24 | 24 |
| `2 + 3 * 4` | 14 | 14 | 20 | 20 |
| `10 - 2 * 3` | 4 | 4 | 24 | 24 |
| `20 / 2 + 3` | 13 | 13 | 4 | 13 |
| `2 * 3 + 4 * 5` | 26 | 26 | 70 | 50 |
| `100 / 10 / 2 + 1` | 6 | 21 | 3.33333 | 6 |
| `2 + 3 * 4 - 5 / 5` | 13 | 13 | -1 | 3 |
| `(2 + 3) * 4` | 20 | 20 | 20 | 20 |
| `2 * (3 + 4)` | 14 | 14 | 14 | 14 |
| `10 - (2 + 3) * 2` | 0 | 0 | 10 | 10 |
| `42` | 42 | 42 | 42 | 42 |
| `7 / 2` | 3.5 | 3.5 | 3.5 | 3.5 |
| `5 / 0` | ERROR semántico | ERROR semántico | ERROR semántico | ERROR semántico |
| `2 + * 3` | RECHAZADA | RECHAZADA | RECHAZADA | RECHAZADA |
| `(2 + 3` | RECHAZADA | RECHAZADA | RECHAZADA | RECHAZADA |

Resumen real: `G1 16/19, G2 16/19, G3 16/19, G4 16/19`
(16 con valor; `5/0` aceptada con error semántico + 2 rechazadas no cuentan).

## Archivos (organizados en subcarpetas)

```
Tarea Análisis de Precedencia y Asociatividad/
  README.md        <- este archivo
  casos.txt        <- combinado: una expresión por línea (# comentario)
  casos_g1.txt     <- G1 (izquierda + correcta): 8 casos con esperados
  casos_g2.txt     <- G2 (derecha + correcta): 8 casos con esperados
  casos_g3.txt     <- G3 (izquierda + invertida): 8 casos con esperados
  casos_g4.txt     <- G4 (plana): 8 casos con esperados
  main.py          <- corre los 4 parsers, grafica los 4 AST y compara
  generar.sh       <- regenera los 4 parsers si se modifica un .g4
  gramatica/       <- las 4 gramáticas
    PrecLeft.g4, PrecRight.g4, PrecInv.g4, PrecFlat.g4
  lab/             <- versión para lab.antlr.org (Start rule: prog; Lexer compartido)
    PrecLabLexer.g4 + G1_PrecLeftLabParser.g4, G2_PrecRightLabParser.g4,
    G3_PrecInvLabParser.g4, G4_PrecFlatLabParser.g4
  generado/        <- código generado con ANTLR 4.13.2 (no editar a mano)
    Prec*Lexer.py, Prec*Parser.py, Prec*Visitor.py, Prec*Listener.py
    (+ .interp/.tokens)
```

- `main.py` agrega `generado/` al `sys.path`, así los imports funcionan
  desde la raíz sin importar la carpeta.

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
cd "Tarea Análisis de Precedencia y Asociatividad"
python3 main.py casos.txt
python3 main.py casos_g1.txt
python3 main.py casos_g2.txt
python3 main.py casos_g3.txt
python3 main.py casos_g4.txt
python3 main.py "4 - 3 - 2"
python3 main.py
```

Sin argumentos usa `casos.txt`. La carpeta tiene espacios: usa comillas.

## Regenerar los parsers

```bash
chmod +x generar.sh
./generar.sh
```

Busca el jar en `$ANTLR_JAR` o `/tmp/antlr-4.13.2-complete.jar`. Descarga:

```bash
curl -L -o /tmp/antlr-4.13.2-complete.jar https://www.antlr.org/download/antlr-4.13.2-complete.jar
```

Se necesita Java 11 o superior (solo para generar, no para ejecutar).
