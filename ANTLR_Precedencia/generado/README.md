# generado/ — Parsers generados por ANTLR (no editar)

Salida de `./generar.sh` (ANTLR 4.13.2, `-Dlanguage=Python3 -visitor -o generado`)
a partir de `../gramatica/*.g4`. `main.py` los importa añadiendo esta
carpeta a `sys.path`, por eso el programa se ejecuta desde la raíz de la tarea.

## Contenido (por cada una de las 4 gramáticas)

`PrecLeft`, `PrecRight`, `PrecInv`, `PrecFlat`, cada una con:

- `*Lexer.py`, `*Parser.py`, `*Visitor.py`, `*Listener.py` (runtime Python)
- `*.interp`, `*.tokens` y `*Lexer.interp`, `*Lexer.tokens` (intermedios de ANTLR)

`__pycache__/` es caché de Python y se puede borrar sin problema.

## Regenerar

Solo si cambia algo en `../gramatica/`, desde la raíz de la tarea:

```bash
./generar.sh
```

Necesita Java 21 y el jar ANTLR 4.13.2
(`$ANTLR_JAR` o `/tmp/antlr-4.13.2-complete.jar`).
Tras regenerar, comprobar con:

```bash
python3 main.py casos.txt
```

Resultado esperado: G1–G4 `8/9` ACEPTADAS (`2 + * 3` RECHAZADA en las 4).
