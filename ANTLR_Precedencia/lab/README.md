# lab/ — Versión para lab.antlr.org (lexer + parser separados)

`lab.antlr.org` pide la gramática en dos pestañas, por eso aquí cada
gramática combinada de `../gramatica/` está partida en dos archivos:
lexer suelto + parser que lo referencia con `tokenVocab`.

## Archivos (el G1–G4 va en el nombre)

| Archivo | Qué es | Corresponde a |
|---|---|---|
| `PrecLabLexer.g4` | Lexer **compartido** por las 4 (`NUM`, `MAS`, `MENOS`, `POR`, `DIV`, `LP`, `RP`, `WS -> skip`). Sin literales sueltos. | Todas |
| `G1_PrecLeftLabParser.g4` | **G1**: izquierda + correcta (`*/ > +-`) | `../gramatica/PrecLeft.g4` |
| `G2_PrecRightLabParser.g4` | **G2**: derecha + correcta (`*/ > +-`) | `../gramatica/PrecRight.g4` |
| `G3_PrecInvLabParser.g4` | **G3**: izquierda + invertida (`+- > */`) | `../gramatica/PrecInv.g4` |
| `G4_PrecFlatLabParser.g4` | **G4**: plana, sin niveles | `../gramatica/PrecFlat.g4` |

Cada parser declara `options { tokenVocab=PrecLabLexer; }` y usa los
tokens (`MAS`, `MENOS`, `POR`, `DIV`, `LP`, `RP`) en lugar de `'+'`,
`'-'`, etc.

## Uso en lab.antlr.org

1. Pestaña **Lexer**: pegar el contenido de `PrecLabLexer.g4`.
2. Pestaña **Parser**: pegar UNO de los cuatro (`G1_`, `G2_`, `G3_` o `G4_`).
3. **Start rule**: `prog`.
4. **Input** de ejemplo: `4 - 3 - 2` (asociatividad) o `2 + 3 * 4` (precedencia).
5. Comparar los árboles entre parsers: el mismo input da agrupaciones
   distintas según la gramática (esa es la demostración de las pruebas 1 y 2).

Estos archivos son solo para la herramienta web: la ejecución real con
`.py` usa los parsers de `../generado/`.
