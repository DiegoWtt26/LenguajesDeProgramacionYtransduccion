# Carpeta generado/

Esta carpeta contiene los archivos que ANTLR genera a partir de las gramáticas de `../gramatica/`. Se crean con `./generar.sh` (ANTLR 4.13.2, `-Dlanguage=Python3 -visitor -o generado`). No se modifican directamente: cualquier cambio se hace en el `.g4` y se vuelve a generar.

`main.py` incluye esta carpeta en el `sys.path` para importar los parsers. Por eso el programa se ejecuta desde la raíz de la tarea.

## Contenido por gramática

Por cada una (`PrecLeft`, `PrecRight`, `PrecInv`, `PrecFlat`):

- `*Lexer.py`, `*Parser.py`, `*Visitor.py`, `*Listener.py`
- `*.interp`, `*.tokens` y `*Lexer.interp`, `*Lexer.tokens` (archivos intermedios de ANTLR)

`__pycache__/` es la caché de Python y se puede borrar sin problema.

## Regenerar

Solo hace falta si cambia algo en `../gramatica/`. Desde la raíz de la tarea:

```bash
./generar.sh
```

Requiere Java 21 y el jar de ANTLR 4.13.2 (`$ANTLR_JAR` o `/tmp/antlr-4.13.2-complete.jar`). Después, comprobación con:

```bash
python3 main.py casos.txt
```

Resultado esperado: G1–G4 con `8/9` ACEPTADAS (`2 + * 3` RECHAZADA en las 4).
