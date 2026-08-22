# Ejercicio 4

## Enunciado del libro

Does the handwritten version of the scanner from Example 1-4 recognize exactly the
same tokens as the flex version?

No, la versión escrita a mano no reconoce exactamente los mismos tokens que la versión
Flex.

La versión Flex del capítulo reconoce `NUMBER`, `ADD`, `SUB`, `MUL`, `DIV`, `ABS`,
`EOL`, `OP` y `CP`, además de ignorar comentarios `//...`. La versión manual mostrada
en el libro reconoce números, operadores aritméticos, `|`, saltos de línea y
comentarios, pero el código mostrado no incluye los casos de paréntesis `(` y `)`.
Por tanto, esos caracteres llegan al caso predeterminado y no producen `OP` ni `CP`.

También hay diferencias prácticas: el scanner manual necesita incluir `<ctype.h>` para
`isdigit`, debe manejar explícitamente todos los caracteres desconocidos y tiene que
mantener el mismo tratamiento de comentarios al final de archivo. Para que fueran
equivalentes habría que añadir al `switch`:

```c
case '(': return OP;
case ')': return CP;
```

y conservar exactamente las mismas reglas para espacios, comentarios, `EOF` y
caracteres inválidos.
