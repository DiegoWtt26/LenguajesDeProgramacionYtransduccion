# Carpeta lab/ — Versión para lab.antlr.org

En `lab.antlr.org` la gramática se pega en dos pestañas separadas (lexer y parser). Por eso cada gramática combinada de `../gramatica/` aquí está dividida en dos archivos: un lexer y un parser que lo usa mediante `tokenVocab`.

## Archivos

| Archivo | Contenido | Gramática base |
|---|---|---|
| `PrecLabLexer.g4` | Lexer compartido por las 4 (`NUM`, `MAS`, `MENOS`, `POR`, `DIV`, `LP`, `RP`, `WS -> skip`). No usa literales como `'+'`. | Todas |
| `G1_PrecLeftLabParser.g4` | G1: asociatividad a izquierda, precedencia correcta (`*/ > +-`) | `../gramatica/PrecLeft.g4` |
| `G2_PrecRightLabParser.g4` | G2: asociatividad a derecha, precedencia correcta (`*/ > +-`) | `../gramatica/PrecRight.g4` |
| `G3_PrecInvLabParser.g4` | G3: asociatividad a izquierda, precedencia invertida (`+- > */`) | `../gramatica/PrecInv.g4` |
| `G4_PrecFlatLabParser.g4` | G4: plana, sin niveles | `../gramatica/PrecFlat.g4` |

Cada parser declara `options { tokenVocab=PrecLabLexer; }` y usa los nombres de tokens (`MAS`, `MENOS`, `POR`, `DIV`, `LP`, `RP`) en lugar de los símbolos `'+'`, `'-'`, etc.

## Uso en lab.antlr.org

1. Pestaña Lexer: pegar el contenido de `PrecLabLexer.g4`.
2. Pestaña Parser: pegar solo uno de los cuatro (`G1_`, `G2_`, `G3_` o `G4_`).
3. Regla inicial (start rule): `prog`.
4. Entrada de prueba: `4 - 3 - 2` (asociatividad) o `2 + 3 * 4` (precedencia).
5. Comparación de los árboles entre parsers: el mismo texto produce distinta agrupación según la gramática.

Estos archivos son solo para la herramienta web. El programa en Python usa los parsers de `../generado/`.
