# Ejercicios del Libro — Flex & Bison

Este repositorio contiene la solución a un conjunto de ejercicios propuestos en el
capítulo sobre Flex y Bison, incluyendo la calculadora de ejemplo del libro, sus
variantes y algunas preguntas teóricas.

## Integrantes

- Camilo Bernal
- Diego Moreno
- Yeisson Rincon


---

## Ejercicio 1 — ¿La calculadora acepta una línea con solo un comentario?

**Pregunta del libro:** *Will the calculator accept a line that contains only a
comment? Why not? Would it be easier to fix this in the scanner or in the parser?*

**Resumen:** No lo acepta, porque la regla de comentarios del scanner original
(`"//".*`) no consume el salto de línea, así que el parser recibe un `EOL` sin una
expresión previa y falla. Es más sencillo arreglarlo en el **scanner**, haciendo que
la regla de comentario también consuma el `\n` (o el fin de archivo).

📄 Ver [`ejercicio_1.md`](ejercicio_1.md) para la explicación completa.

---

## Ejercicio 2 — Calculadora hexadecimal

**Pregunta del libro:** *Make the calculator into a hex calculator that accepts both
hex and decimal numbers... use `strtol`... print the result in both decimal and hex.*

**Resumen:** Se añadió al scanner (`ejercicio_2.l`) una regla para reconocer números
en formato hexadecimal (`0x...`) y otra para decimales, ambas usando `strtol` para
convertir el texto a entero. El parser (`ejercicio_2.y`) imprime el resultado con
`printf("= %d (0x%X)\n", ...)`, mostrando el valor en decimal y en hexadecimal.

**Compilación y ejecución:**

```bash
bison -d ejercicio_2.y
flex ejercicio_2.l
gcc ejercicio_2.tab.c lex.yy.c -o eje2 -lfl
./eje2
```

**Captura de ejecución:**

![Ejecución ejercicio 2](capturas/ejercicio_2_ejecucion.png)

Como se observa, `0x10 + 10` produce `= 26 (0x1A)`.

📄 Ver [`ejercicio_2.md`](ejercicio_2.md) para el código completo y la explicación.

---

## Ejercicio 3 — Operadores bit a bit (AND / OR)

**Pregunta del libro:** *(extra credit) Add bit operators such as AND and OR to the
calculator. The obvious operator to use for OR is a vertical bar, but that's already
the unary absolute value operator...*

**Resumen:** Se agregó el operador `&` (AND) y se reutilizó el carácter `|` tanto para
el valor absoluto unario (`|numero`) como para el OR binario (`exp | factor`). La
ambigüedad se resuelve en la gramática: el token `ABS` es unario solo cuando aparece
al inicio de un `term`, y binario cuando aparece entre dos expresiones (`exp`). Bison
no reporta conflictos porque los niveles de precedencia (`exp`, `factor`, `term`)
separan claramente ambos casos.

**Compilación y ejecución:**

```bash
bison -d ejercicio_3.y
flex ejercicio_3.l
gcc ejercicio_3.tab.c lex.yy.c -o eje3 -lfl
./eje3
```

**Captura de ejecución:**

![Ejecución ejercicio 3](capturas/ejercicio_3_ejecucion.png)

En la captura se observa `|8` (valor absoluto) devolviendo `= 8`, y `5 | 3` (OR
binario) devolviendo `= 7`.

📄 Ver [`ejercicio_3.md`](ejercicio_3.md) para el código completo y la explicación.

---

## Ejercicio 4 — Scanner escrito a mano vs. scanner con Flex

**Pregunta del libro:** *Does the handwritten version of the scanner from Example 1-4
recognize exactly the same tokens as the flex version?*

**Resumen:** No son equivalentes. El scanner escrito a mano del libro no maneja los
paréntesis `(` y `)`, por lo que no genera los tokens `OP` y `CP` que sí produce la
versión Flex. Para igualarlos habría que añadir esos casos al `switch` y mantener el
mismo tratamiento de espacios, comentarios, `EOF` y caracteres inválidos.

📄 Ver [`ejercicio_4.md`](ejercicio_4.md) para la explicación completa.

---

## Ejercicio 5 — Límites de Flex para ciertos lenguajes

**Pregunta del libro:** *Can you think of languages for which flex wouldn't be a good
tool to write a scanner?*

**Resumen:** Flex no es adecuado cuando el reconocimiento de un token depende de
contexto que no puede expresarse con expresiones regulares: lenguajes sensibles a la
indentación (Python, Haskell), comentarios anidados, identificadores que son palabra
reservada según el contexto, lenguajes con dependencia semántica, o lenguajes
naturales.

📄 Ver [`ejercicio_5.md`](ejercicio_5.md) para la explicación completa.

---

## Ejercicio 6 — Conteo de palabras en C vs. Flex

**Pregunta del libro:** *Rewrite the word count program in C. Run some large files
through both versions. Is the C version noticeably faster? How much harder was it to
debug?*

**Resumen:** Se reescribió el programa de conteo de palabras (líneas, palabras y
caracteres) directamente en C, sin usar Flex, replicando la misma definición de
palabra (`[a-zA-Z]+`). El programa en C es más trabajoso de depurar porque hay que
manejar manualmente el estado (dentro/fuera de una palabra), mientras que Flex expresa
las reglas de forma más directa y declarativa. En archivos grandes, ambas versiones
producen los mismos conteos; la diferencia de velocidad suele ser pequeña, aunque la
versión en C puede ser ligeramente más rápida al evitar la capa del scanner generado.

**Compilación y ejecución:**

```bash
gcc ejercicio_6.c -o eje6
./eje6
```

**Captura de ejecución:**

![Ejecución ejercicio 6](capturas/ejercicio_6_ejecucion.png)

📄 Ver [`ejercicio_6.c`](ejercicio_6.c) para el código y los comentarios de
comparación con la versión Flex.

---

## Requisitos

- `flex`
- `bison`
- `gcc`

## Cómo compilar todo desde cero

```bash
# Ejercicio 2
bison -d ejercicio_2.y
flex ejercicio_2.l
gcc ejercicio_2.tab.c lex.yy.c -o eje2 -lfl

# Ejercicio 3
bison -d ejercicio_3.y
flex ejercicio_3.l
gcc ejercicio_3.tab.c lex.yy.c -o eje3 -lfl

# Ejercicio 6
gcc ejercicio_6.c -o eje6
```
