# Carpeta gramatica/ — Gramáticas fuente (.g4)

Aquí están las 4 gramáticas del lenguaje (`+ - * / ( )`, `NUM` entero o decimal, división real). Son gramáticas combinadas (lexer + parser en el mismo archivo). La regla inicial en las 4 es `prog : e EOF ;`.

| Archivo | Diseño | Explicación |
|---|---|---|
| `PrecLeft.g4` (G1) | Asociatividad a izquierda, precedencia correcta | `e : e op t \| t`, `t : t op f \| f`. Los niveles `e/t/f` hacen que `* /` tenga más prioridad que `+ -`. Es la gramática de referencia. |
| `PrecRight.g4` (G2) | Asociatividad a derecha, precedencia correcta | `e : t op e \| t`, `t : f op t \| f`. Agrupa hacia la derecha, pero `* /` sigue con más prioridad. |
| `PrecInv.g4` (G3) | Asociatividad a izquierda, precedencia invertida | Igual que G1 pero con los niveles cruzados: `+ -` tiene más prioridad que `* /`. Sirve para comparar qué pasa si la precedencia está al revés. |
| `PrecFlat.g4` (G4) | Sin niveles | `expr : atom (op atom)*` con pliegue a izquierda en el visitor. Todos los operadores quedan al mismo nivel y se evalúan en orden de lectura. |

## Pruebas base

1. Asociatividad: `4 - 3 - 2` → G1/G3/G4 dan `-1` `((4-3)-2)`; G2 da `3` `(4-(3-2))`.
2. Precedencia: `2 + 3 * 4` → G1/G2 dan `14` (`2+(3*4)`); G3/G4 dan `20` (`(2+3)*4`).
3. AST: `main.py` muestra el árbol en ASCII y en tupla para cada gramática y cada caso.

## Regenerar

Los cambios del lenguaje se hacen solo en esta carpeta. Después, desde la raíz de la tarea:

```bash
./generar.sh
```

Requiere Java 21 y `antlr-4.13.2-complete.jar`. El resultado se guarda en `../generado/`.
