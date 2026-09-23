# Precedencia y asociatividad (Linux)

## Integrantes

- Camilo Bernal
- Diego Moreno
- Yeisson Rincón

## Las 4 gramáticas

Mismo lenguaje en las 4 (`+ - * /`, paréntesis, `NUM`, división real):

| ID | Reglas clave | Asociatividad | Precedencia |
|----|--------------|---------------|-------------|
| G1 `PrecLeft.g4` | `e:e op t \| t` , `t:t op f \| f` | izquierda | correcta: `*/ > +-` (diapos 27, 30) |
| G2 `PrecRight.g4` | `e:t op e \| t` , `t:f op t \| f` | derecha (diapo 28: `E → T op E`) | correcta: `*/ > +-` |
| G3 `PrecInv.g4` | `e:e */ t \| t` , `t:t +- f \| f` | izquierda | invertida: `+- > */` |
| G4 `PrecFlat.g4` | `expr: atom (op atom)*` | izquierda | sin niveles, pliegue izquierda-derecha |

G1 como referencia. G2 con cambio de dirección, G3 con niveles cruzados, G4 sin niveles.

## Salida de `main.py`

Ejecución de las 4 gramáticas por línea del txt. Por cada una: `Estado` (ACEPTADA / RECHAZADA), AST en ASCII, AST en tupla y evaluación. Comparativa final:

- **Asociatividad G1 vs G2** (diapo 27): `4 - 3 - 2`, G1 `(4-3)-2 = -1`, G2 `4-(3-2) = 3`. Distinto árbol, distinto valor.
- **Precedencia G1 vs G3 vs G4** (diapos 29–30): `2 + 3 * 4`, G1 `2+(3*4) = 14`, G3 `(2+3)*4 = 20`, G4 `20` (orden de lectura).
- Caso `2 * 3 + 4 * 5`: G1 = 26, G3 = 70, G4 = 50.
- Paréntesis en las 4: `(2+3)*4 = 20`, `2*(3+4) = 14`.

## Archivos de casos: 1 general + 4 dedicados

`casos.txt` como único comparativo (13 casos, 4 bloques). Cada `casos_gN.txt` como dedicado, con valor solo de su gramática. `main.py` con ejecución de las 4 en todos los casos; el `# =>` de cada dedicado indica solo lo esperado en esa.

| archivo | fenómeno (PDF) | casos |
|---------|------------------------------|-------|
| `casos_g1.txt` | G1 referencia: izquierda + correcta (diapos 27, 29, 30) | 10 (9 con valor + 1 rechazado) |
| `casos_g2.txt` | G2: agrupación derecha (diapo 28) | 8 (7 con valor + 1 rechazado) |
| `casos_g3.txt` | G3: niveles invertidos (diapos 29-30) | 8 (7 con valor + 1 rechazado) |
| `casos_g4.txt` | G4: sin niveles, pliegue plano | 8 (7 con valor + 1 rechazado) |

Tabla con `casos.txt` (general):

| caso | G1 izq-ok | G2 der-ok | G3 invertida | G4 plana |
|------|-----------|-----------|--------------|----------|
| `4 - 3 - 2` | -1 | 3 | -1 | -1 |
| `8 / 4 / 2` | 1 | 4 | 1 | 1 |
| `2 + 3 * 4` | 14 | 14 | 20 | 20 |
| `10 - 2 * 3` | 4 | 4 | 24 | 24 |
| `2 * 3 + 4 * 5` | 26 | 26 | 70 | 50 |
| `2 + 3 * 4 - 5 / 5` | 13 | 13 | -1 | 3 |
| `(2 + 3) * 4` | 20 | 20 | 20 | 20 |
| `2 * (3 + 4)` | 14 | 14 | 14 | 14 |
| `42` | 42 | 42 | 42 | 42 |
| `7 / 2` | 3.5 | 3.5 | 3.5 | 3.5 |
| `5 / 0` | ERROR semántico | ERROR semántico | ERROR semántico | ERROR semántico |
| `2 + * 3` | RECHAZADA | RECHAZADA | RECHAZADA | RECHAZADA |
| `(2 + 3` | RECHAZADA | RECHAZADA | RECHAZADA | RECHAZADA |

Resumen general: `G1 10/13, G2 10/13, G3 10/13, G4 10/13` (10 con valor; `5/0` con error semántico + 2 rechazadas). Dedicados: `casos_g1.txt` 9/10, resto 7/8.

## Archivos (subcarpetas)

```
ANTLR_Precedencia/
  README.md        <- este archivo
  casos.txt        <- general comparativo
  casos_g1.txt     <- G1: 10 casos
  casos_g2.txt     <- G2: 8 casos
  casos_g3.txt     <- G3: 8 casos
  casos_g4.txt     <- G4: 8 casos
  main.py          <- ejecución de los 4 parsers + comparativa
  generar.sh       <- regeneración
  gramatica/       <- las 4 gramáticas
  lab/             <- versión lab.antlr.org (start: prog)
  generado/        <- código generado por ANTLR 4.13.2 (se crea con generar.sh, no se edita a mano)
```

`main.py` incluye `generado/` en el `sys.path` para importar los parsers. El programa se ejecuta desde la raíz.

## Requisitos

```bash
python3 --version   # >= 3.10
pip3 install antlr4-python3-runtime==4.13.2
```

Con entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install antlr4-python3-runtime==4.13.2
```

## Ejecución

```bash
cd ANTLR_Precedencia
python3 main.py casos.txt
python3 main.py casos_g1.txt
python3 main.py casos_g2.txt
python3 main.py casos_g3.txt
python3 main.py casos_g4.txt
python3 main.py "4 - 3 - 2"
python3 main.py
```

Sin argumentos, uso de `casos.txt`.

## Regenerar

```bash
chmod +x generar.sh
./generar.sh
```

Búsqueda del jar en `$ANTLR_JAR` o `/tmp/antlr-4.13.2-complete.jar`:

```bash
curl -L -o /tmp/antlr-4.13.2-complete.jar https://www.antlr.org/download/antlr-4.13.2-complete.jar
```

Java 11 o superior (solo generación, no ejecución).
