# Ejercicios del libro — Flex & Bison

Soluciones a ejercicios del capítulo sobre Flex y Bison: calculadora del libro, variantes y preguntas teóricas.

## Integrantes

- Camilo Bernal
- Diego Moreno
- Yeisson Rincón

---

## Ejercicio 1 — ¿Acepta una línea con solo un comentario?

**Pregunta del libro:** *Will the calculator accept a line that contains only a comment? Why not? Would it be easier to fix this in the scanner or in the parser?*

**Resumen:** La calculadora no acepta esa línea. La regla de comentarios (`"//".*`) no consume el salto de línea, por lo que el parser recibe un `EOL` sin una expresión previa y la línea falla. La corrección más simple se hace en el scanner, haciendo que la regla de comentario también consuma el `\n` (o el fin de archivo).

📄 Detalle en [`ejercicio_1.md`](ejercicio_1.md).

---

## Ejercicio 2 — Calculadora hexadecimal

**Pregunta del libro:** *Make the calculator into a hex calculator that accepts both hex and decimal numbers... use `strtol`... print the result in both decimal and hex.*

**Resumen:** En `ejercicio_2.l` se agrega una regla para números hexadecimales (`0x...`) y otra para decimales, ambas con conversión mediante `strtol`. En `ejercicio_2.y` la salida usa `printf("= %d (0x%X)\n", ...)`, de modo que el valor se presenta en decimal y en hexadecimal.

**Compilación y ejecución:**

```bash
bison -d ejercicio_2.y
flex ejercicio_2.l
gcc ejercicio_2.tab.c lex.yy.c -o eje2 -lfl
./eje2
```

![Ejecución ejercicio 2](capturas/ejercicio_2_ejecucion.png)

Por ejemplo, la entrada `0x10 + 10` produce `= 26 (0x1A)`.

📄 Código y explicación en [`ejercicio_2.md`](ejercicio_2.md).

---

## Ejercicio 3 — Operadores bit a bit (AND / OR)

**Pregunta del libro:** *(extra credit) Add bit operators such as AND and OR to the calculator...*

**Resumen:** Se agrega el operador `&` (AND) y se le da doble uso al carácter `|`: valor absoluto unario (`|numero`) y OR binario (`exp | factor`). La ambigüedad se resuelve en la gramática: el token `ABS` es unario solo al inicio de un `term`, y binario cuando aparece entre dos `exp`. Bison no reporta conflictos porque los niveles (`exp`, `factor`, `term`) separan ambos casos.

**Compilación y ejecución:**

```bash
bison -d ejercicio_3.y
flex ejercicio_3.l
gcc ejercicio_3.tab.c lex.yy.c -o eje3 -lfl
./eje3
```

![Ejecución ejercicio 3](capturas/ejercicio_3_ejecucion.png)

Por ejemplo, `|8` (valor absoluto) produce `= 8`, y `5 | 3` (OR binario) produce `= 7`.

📄 Código y explicación en [`ejercicio_3.md`](ejercicio_3.md).

---

## Ejercicio 4 — Scanner manual vs Flex

**Pregunta del libro:** *Does the handwritten version of the scanner from Example 1-4 recognize exactly the same tokens as the flex version?*

**Resumen:** Las dos versiones no son equivalentes. La versión manual no maneja los paréntesis `(` y `)`, así que no produce los tokens `OP` y `CP` que sí genera la versión Flex. Para igualarlas, se agregan esos casos al `switch` manteniendo el mismo tratamiento de espacios, comentarios, `EOF` y caracteres inválidos.

📄 Detalle en [`ejercicio_4.md`](ejercicio_4.md).

---

## Ejercicio 5 — Límites de Flex

**Pregunta del libro:** *Can you think of languages for which flex wouldn't be a good tool to write a scanner?*

**Resumen:** Flex no es una buena herramienta cuando el reconocimiento de un token depende de un contexto que no se puede expresar con expresiones regulares: lenguajes sensibles a la indentación (Python, Haskell), comentarios anidados, identificadores que son palabra reservada según el contexto, lenguajes con dependencia semántica o el lenguaje natural.

📄 Detalle en [`ejercicio_5.md`](ejercicio_5.md).

---

## Ejercicio 6 — Conteo en C vs Flex

**Pregunta del libro:** *Rewrite the word count program in C. Run some large files through both versions. Is the C version noticeably faster? How much harder was it to debug?*

**Resumen:** El programa de conteo (líneas, palabras y caracteres) se reescribe directamente en C, sin Flex, definiendo palabra como `[a-zA-Z]+`. En C el estado se maneja de forma manual (dentro o fuera de una palabra), mientras que en Flex las reglas son declarativas y directas. En archivos grandes ambas versiones producen los mismos conteos. La diferencia de velocidad es reducida (la versión en C es apenas más rápida al evitar la capa del scanner generado), pero la depuración resulta más costosa en C.

**Compilación y ejecución:**

```bash
gcc ejercicio_6.c -o eje6
./eje6
```

![Ejecución ejercicio 6](capturas/ejercicio_6_ejecucion.png)

📄 Código en [`ejercicio_6.c`](ejercicio_6.c).

---

## Requisitos

- `flex`
- `bison`
- `gcc`

## Compilación total

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
