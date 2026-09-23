# gramatica/ — Las 4 gramáticas (.g4 fuente)

Fuentes ANTLR combinadas (parser + lexer) del mismo lenguaje:
`+ - * / ( )`, `NUM` (entero o decimal), división real. Regla inicial: `prog : e EOF ;`.

| Archivo | Diseño | Idea (diapos 27–31) |
|---|---|---|
| `PrecLeft.g4` (G1) | Izquierda + correcta | `e : e op t \| t`, `t : t op f \| f`. Patrón `E → E op T` = izquierda; niveles `e/t/f` = `* /` sobre `+ -`. Referencia. |
| `PrecRight.g4` (G2) | Derecha + correcta | `e : t op e \| t`, `t : f op t \| f`. Patrón `E → T op E` = derecha. Niveles con `* /` arriba. |
| `PrecInv.g4` (G3) | Izquierda + invertida | Misma forma G1 con niveles cruzados: `+ -` sobre `* /`. Prueba de precedencia invertida. |
| `PrecFlat.g4` (G4) | Plana, sin niveles | `expr : atom (op atom)*` con pliegue a izquierda en el visitor. Mismo nivel para todo, orden de lectura. |

## Pruebas base

1. Asociatividad (diapo 27): `4 - 3 - 2` → G1/G3/G4 `-1` `((4-3)-2)`; G2 `3` `(4-(3-2))`.
2. Precedencia (diapos 29–30): `2 + 3 * 4` → G1/G2 `14` (`2+(3*4)`); G3/G4 `20` (`(2+3)*4`).
3. AST: gráfico ASCII + tupla por gramática y caso en `main.py`.

## Regenerar

Cambios de lenguaje solo en esta carpeta. Desde la raíz:

```bash
./generar.sh
```

Requisito: Java 21 + `antlr-4.13.2-complete.jar`. Salida en `../generado/`.
