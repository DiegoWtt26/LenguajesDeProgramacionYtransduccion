# generado/ — Parsers generados por ANTLR (sin edición)

Salida de `./generar.sh` (ANTLR 4.13.2, `-Dlanguage=Python3 -visitor -o generado`) desde `../gramatica/*.g4`. Import en `main.py` con agregado de esta carpeta a `sys.path`. Ejecución desde la raíz.

## Contenido (por cada gramática)

`PrecLeft`, `PrecRight`, `PrecInv`, `PrecFlat`, cada una con:

- `*Lexer.py`, `*Parser.py`, `*Visitor.py`, `*Listener.py`
- `*.interp`, `*.tokens` y `*Lexer.interp`, `*Lexer.tokens`

`__pycache__/` como caché de Python, borrado sin efecto.

## Regenerar

Solo con cambios en `../gramatica/`, desde la raíz:

```bash
./generar.sh
```

Requisito: Java 21 + jar ANTLR 4.13.2 (`$ANTLR_JAR` o `/tmp/antlr-4.13.2-complete.jar`). Comprobación:

```bash
python3 main.py casos.txt
```

Resultado: G1–G4 `8/9` ACEPTADAS (`2 + * 3` RECHAZADA en las 4).
