# Ejercicio 5

## Enunciado del libro

Can you think of languages for which flex wouldn’t be a good tool to write a scanner?

Flex no es una buena elección cuando el reconocimiento de un token depende de
información que no puede expresarse de forma regular o requiere contexto amplio.

Ejemplos:

- Python y Haskell, porque la indentación cambia la estructura léxica y obliga a
  mantener una pila de niveles y generar tokens artificiales.
- Lenguajes con comentarios anidados, porque una expresión regular simple no cuenta
  arbitrariamente la profundidad de anidamiento.
- Lenguajes donde un identificador puede ser palabra reservada dependiendo de su
  declaración o del ámbito actual.
- Lenguajes con sintaxis léxica dependiente de tipos, declaraciones previas o análisis
  semántico.
- Lenguajes naturales, por la ambigüedad y la dependencia del contexto.

Flex puede ampliarse con estados y código C auxiliar, pero en esos casos deja de ser la
herramienta sencilla que se busca para una especificación léxica regular. Conviene usar
un lexer con soporte explícito para estados, una rutina manual o dejar parte del trabajo
al parser y al análisis semántico.
