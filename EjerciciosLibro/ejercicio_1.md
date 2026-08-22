# Ejercicio 1

## Enunciado del libro

Will the calculator accept a line that contains only a comment? Why not? Would it be
easier to fix this in the scanner or in the parser?

## Respuesta

No, La regla del scanner que ignora comentarios (`"//".*`) no consume el salto de
línea. Después del comentario el scanner devuelve `EOL`, pero el parser espera una
expresión seguida de `EOL`. Por eso una línea que contiene únicamente un comentario
produce un error de sintaxis.

Es más sencillo corregirlo en el scanner, porque el comentario es un detalle léxico.
La regla debe consumir también el salto de línea:

```lex
"//"[^\n]*\n    { /* ignora el comentario y su fin de línea */ }
```

Así, una línea que solo contiene un comentario no genera ningún token y el parser
puede continuar con la siguiente línea. También funciona un comentario al final del
archivo sin salto de línea si se añade esta regla:

```lex
"//"[^\n]*    { /* ignora comentario hasta EOF */ }
```
