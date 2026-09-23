# lab/ — Versión para lab.antlr.org (lexer + parser separados)

`lab.antlr.org` con gramática en dos pestañas. Cada combinada de `../gramatica/` en dos archivos: lexer + parser con `tokenVocab`.

## Archivos

| Archivo | Contenido | Base |
|---|---|---|
| `PrecLabLexer.g4` | Lexer compartido (`NUM`, `MAS`, `MENOS`, `POR`, `DIV`, `LP`, `RP`, `WS -> skip`). Sin literales. | Todas |
| `G1_PrecLeftLabParser.g4` | G1: izquierda + correcta (`*/ > +-`) | `../gramatica/PrecLeft.g4` |
| `G2_PrecRightLabParser.g4` | G2: derecha + correcta (`*/ > +-`) | `../gramatica/PrecRight.g4` |
| `G3_PrecInvLabParser.g4` | G3: izquierda + invertida (`+- > */`) | `../gramatica/PrecInv.g4` |
| `G4_PrecFlatLabParser.g4` | G4: plana, sin niveles | `../gramatica/PrecFlat.g4` |

Cada parser con `options { tokenVocab=PrecLabLexer; }` y tokens (`MAS`, `MENOS`, `POR`, `DIV`, `LP`, `RP`) en lugar de `'+'`, `'-'`, etc.

## Uso en lab.antlr.org

1. Pestaña Lexer: contenido de `PrecLabLexer.g4`.
2. Pestaña Parser: uno de los cuatro (`G1_`, `G2_`, `G3_` o `G4_`).
3. Start rule: `prog`.
4. Input: `4 - 3 - 2` (asociatividad) o `2 + 3 * 4` (precedencia).
5. Comparación de árboles entre parsers: mismo input, distinta agrupación según gramática.

Archivos solo para la herramienta web. Ejecución `.py` con parsers de `../generado/`.
