# Precedencia y asociatividad (Linux)

## Integrantes

- Camilo Bernal
- Diego Moreno
- Yeisson Rincón

Trabajo sobre precedencia y asociatividad con cuatro gramáticas del mismo lenguaje (`+ - * /`, paréntesis, `NUM` y división real). Todo el trabajo está probado en Linux con bash.

## Las 4 gramáticas

| ID | Reglas clave | Asociatividad | Precedencia |
|----|--------------|---------------|-------------|
| G1 `PrecLeft.g4` | `e:e op t \| t` , `t:t op f \| f` | izquierda | correcta: `*/ > +-` |
| G2 `PrecRight.g4` | `e:t op e \| t` , `t:f op t \| f` | derecha | correcta: `*/ > +-` |
| G3 `PrecInv.g4` | `e:e */ t \| t` , `t:t +- f \| f` | izquierda | invertida a propósito: `+- > */` |
| G4 `PrecFlat.g4` | `expr: atom (op atom)*` | izquierda | sin niveles: todo se evalúa de izquierda a derecha |

G1 es la gramática de referencia. G2 cambia únicamente la dirección de la recursión, G3 intercambia los niveles de precedencia y G4 elimina los niveles por completo.

## Salida de `main.py`

Por cada línea del archivo de casos, el programa ejecuta las 4 gramáticas. Para cada una muestra el `Estado` (ACEPTADA o RECHAZADA), el AST en ASCII, el AST en tupla y el valor evaluado. Al final presenta la comparación:

- **Asociatividad G1 vs G2**: con `4 - 3 - 2`, G1 produce `(4-3)-2 = -1` y G2 produce `4-(3-2) = 3`. El mismo texto genera árboles distintos y valores distintos.
- **Precedencia G1 vs G3 vs G4**: con `2 + 3 * 4`, G1 produce `2+(3*4) = 14`, mientras que G3 produce `(2+3)*4 = 20` por tener los niveles invertidos, y G4 también produce `20` porque evalúa de izquierda a derecha.
- El caso `2 * 3 + 4 * 5` es el que más diferencia las tres variantes: G1 da 26, G3 da 70 y G4 da 50.
- Los paréntesis tienen prioridad en las 4 gramáticas: `(2+3)*4 = 20` y `2*(3+4) = 14`.

## Archivos de casos: 1 general + 4 dedicados

El archivo `casos.txt` es el único comparativo (13 casos organizados en 4 bloques, mezclados a propósito). Cada archivo `casos_gN.txt` está dedicado a su gramática: el comentario `# =>` indica únicamente el valor esperado en esa gramática. El programa `main.py` siempre ejecuta las 4 para poder comparar.

| archivo | fenómeno que demuestra | casos |
|---------|------------------------------|-------|
| `casos_g1.txt` | G1 como referencia: asociatividad a izquierda y precedencia correcta | 10 (9 con valor + 1 rechazado) |
| `casos_g2.txt` | G2: la asociatividad a derecha agrupa al revés | 8 (7 con valor + 1 rechazado) |
| `casos_g3.txt` | G3: niveles de precedencia invertidos | 8 (7 con valor + 1 rechazado) |
| `casos_g4.txt` | G4: sin niveles, evaluación plana de izquierda a derecha | 8 (7 con valor + 1 rechazado) |

Tabla de resultados esperados con `casos.txt` (general, 13 casos en 4 bloques):

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

En resumen: `G1 10/13, G2 10/13, G3 10/13, G4 10/13` (10 casos con valor numérico; el caso `5/0` se acepta pero con error semántico, y 2 casos son rechazados). En los dedicados: `casos_g1.txt` 9/10, y `casos_g2.txt`, `casos_g3.txt`, `casos_g4.txt` 7/8 cada uno.

## Archivos (organizados en subcarpetas)

```
ANTLR_Precedencia/
  README.md        <- este archivo
  casos.txt        <- archivo general comparativo (13 casos)
  casos_g1.txt     <- casos de G1 (10 casos)
  casos_g2.txt     <- casos de G2 (8 casos)
  casos_g3.txt     <- casos de G3 (8 casos)
  casos_g4.txt     <- casos de G4 (8 casos)
  main.py          <- ejecuta los 4 parsers, muestra los 4 AST y presenta la comparación
  generar.sh       <- regenera los 4 parsers si se modifica algún .g4
  gramatica/       <- las 4 gramáticas fuente
  lab/             <- versión para lab.antlr.org (regla inicial: prog)
  generado/        <- código generado por ANTLR 4.13.2 (se crea con generar.sh, no se edita a mano)
```

El archivo `main.py` incluye la carpeta `generado/` en el `sys.path` para importar los parsers. Por eso el programa se ejecuta desde la raíz de la tarea.

## Requisitos

```bash
python3 --version   # 3.10 o superior
pip3 install antlr4-python3-runtime==4.13.2
```

Con entorno virtual (opción recomendada):

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

Si no se indica ningún argumento, el programa utiliza el archivo `casos.txt`.

## Regeneración de los parsers

```bash
chmod +x generar.sh
./generar.sh
```

El script busca el archivo jar en la variable `$ANTLR_JAR` o en la ruta `/tmp/antlr-4.13.2-complete.jar`. Si no existe, se descarga con:

```bash
curl -L -o /tmp/antlr-4.13.2-complete.jar https://www.antlr.org/download/antlr-4.13.2-complete.jar
```

Se necesita Java 11 o superior (únicamente para generar los parsers, no para ejecutarlos).
