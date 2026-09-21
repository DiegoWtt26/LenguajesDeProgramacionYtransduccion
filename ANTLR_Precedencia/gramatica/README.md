# gramatica/ — Las 4 gramáticas (.g4 fuente)

Fuentes ANTLR combinadas (parser + lexer) del mismo lenguaje:
`+  -  *  /  (  )`, operandos `NUM` (entero o decimal), división real (float).
Regla inicial en las 4: `prog : e EOF ;`.

| Archivo | Diseño | Idea (PDF diapos 27–31) |
|---|---|---|
| `PrecLeft.g4` (G1) | Izquierda + precedencia **correcta** | `e : e op t \| t`, `t : t op f \| f`. Patrón `E → E operador T` = asociatividad por la izquierda; niveles `e/t/f` = `* /` atan más fuerte que `+ -`. Es la referencia correcta. |
| `PrecRight.g4` (G2) | Derecha + precedencia **correcta** | `e : t op e \| t`, `t : f op t \| f`. Patrón `E → T operador E` = asociatividad por la derecha. Los niveles siguen dando `* /` mayor precedencia. |
| `PrecInv.g4` (G3) | Izquierda + precedencia **invertida** | Misma forma que G1 pero con los niveles cruzados: `+ -` atan más fuerte que `* /`. Sirve para la prueba 2 (precedencia `+,-,*,/` VS `/,*,-,+`). |
| `PrecFlat.g4` (G4) | **Plana**, sin niveles | `expr : atom (op atom)*` con pliegue a izquierda en el visitor. Todos los operadores al mismo nivel: ni precedencia ni asociatividad real, solo orden de lectura. |

## Pruebas que sostienen

1. **Asociatividad izquierda VS derecha** (diapo 27): `4 - 3 - 2` → G1/G3/G4 dan `-1` `((4-3)-2)`; G2 da `3` `(4-(3-2))`.
2. **Precedencia** (diapos 29–30): `2 + 3 * 4` → G1/G2 dan `14` (`2+(3*4)`); G3/G4 dan `20` (`(2+3)*4`).
3. **AST**: `main.py` grafica (ASCII + tupla) un árbol por gramática para cada caso de `casos.txt`.

## Regenerar

No se edita nada fuera de aquí para cambiar el lenguaje. Tras editar, desde la raíz de la tarea:

```bash
./generar.sh
```

Requiere Java 21 + `antlr-4.13.2-complete.jar`. La salida va a `../generado/`.
