# Actividad ANTLR 4 — Lenguaje de instrucciones

## Integrantes

- Camilo Bernal
- Diego Moreno
- Yeisson Rincón

## Descripción

Lenguaje simple construido con ANTLR 4, capaz de reconocer instrucciones del tipo:
`mostrar ventas`, `cargar clientes` y `graficar ingresos`.

## Gramática

La gramática completa se encuentra en el archivo `Instruccion.g4`:

```antlr
grammar Instruccion;

programa
    : instruccion+ EOF
    ;

instruccion
    : MOSTRAR ID
    | CARGAR ID
    | GRAFICAR ID
    ;

MOSTRAR
    : 'mostrar'
    ;

CARGAR
    : 'cargar'
    ;

GRAFICAR
    : 'graficar'
    ;

ID
    : [a-zA-Z]+
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
```

## Explicación de las reglas léxicas

- **MOSTRAR, CARGAR, GRAFICAR**: reconocen literalmente las palabras clave `mostrar`, `cargar` y `graficar`. Los nombres empiezan con mayúscula porque ANTLR exige que toda regla léxica (token) inicie con letra mayúscula.
- **ID**: reconoce uno o más caracteres alfabéticos (`[a-zA-Z]+`) y se usa para los nombres que acompañan a cada instrucción (ventas, clientes, ingresos, etc.).
- **WS**: reconoce espacios, tabulaciones y saltos de línea, y usa la acción `-> skip` para indicarle al lexer que los descarte y no los envíe al parser.

## Explicación de las reglas sintácticas

- **programa**: es la regla inicial. Indica que un programa válido está compuesto por una o más instrucciones (`instruccion+`) seguidas del fin de archivo (`EOF`). Esto permite procesar varias instrucciones en un mismo archivo de entrada.
- **instruccion**: define que cada instrucción válida está formada por una palabra clave (`MOSTRAR`, `CARGAR` o `GRAFICAR`) seguida de un identificador (`ID`).

## Evidencia de tokens reconocidos

Archivo de entrada: `pruebas_validas.txt` (5 pruebas).

Comando ejecutado:

```
grun Instruccion programa -tokens pruebas_validas.txt
```

Resultado:

![Tokens reconocidos](tokens.png)

## Evidencia del árbol sintáctico

Comando ejecutado:

```
grun Instruccion programa -tree pruebas_validas.txt
```

Resultado:

![Árbol sintáctico en texto](arbol_texto.png)

![Árbol sintáctico gráfico](arbol_grafico.png)

## Casos de error identificados

**Error 1** — orden incorrecto de los tokens (`error1.txt`: `ventas mostrar`)

![Error 1](error1.png)

**Error 2** — instrucción incompleta, falta el identificador (`error2.txt`: `graficar`)

![Error 2](error2.png)

**Error 3** — palabra clave no definida en la gramática (`error3.txt`: `eliminar ventas`)

![Error 3](error3.png)

## Diferencia entre lexer y parser

El lexer y el parser cumplen roles distintos y complementarios dentro del análisis del lenguaje. El lexer trabaja sobre los caracteres: agrupa el texto en unidades con significado (tokens) como palabras clave e identificadores, y descarta lo que no aporta estructura, como los espacios en blanco. El parser, en cambio, trabaja sobre los tokens: verifica que la secuencia generada por el lexer cumpla el orden y la estructura de las reglas sintácticas, y construye el árbol sintáctico correspondiente. En resumen, el lexer responde a la pregunta "¿qué es cada parte del texto?" y el parser responde a "¿estas partes están organizadas correctamente?". Esta separación permite diseñar y depurar cada etapa por separado, y es la base sobre la que se construyen compiladores e intérpretes.

## Preguntas de análisis

**1. ¿Cuál es la diferencia entre un lexema y un token?**
Un lexema es la secuencia de caracteres tal como aparece en el texto de entrada (por ejemplo, la palabra `mostrar`). Un token es la categoría que el lexer le asigna a ese lexema (por ejemplo, `MOSTRAR`). Un mismo token puede corresponder a distintos lexemas (el token `ID` agrupa lexemas como `ventas`, `clientes`, etc.).

**2. ¿Cuál es la responsabilidad del lexer?**
Convierte la secuencia de caracteres del archivo de entrada en una secuencia de tokens: agrupa los caracteres relacionados y descarta los que no son relevantes para el análisis (como los espacios en blanco).

**3. ¿Cuál es la responsabilidad del parser?**
Recibe la secuencia de tokens generada por el lexer y verifica que cumpla la estructura definida por las reglas sintácticas de la gramática. Con esa verificación construye el árbol sintáctico que representa la estructura de la entrada.

**4. ¿Por qué las reglas léxicas comienzan con mayúscula en ANTLR?**
Es una convención de ANTLR que permite diferenciar las reglas léxicas (tokens) de las reglas sintácticas dentro del mismo archivo de gramática.

**5. ¿Por qué las reglas sintácticas comienzan con minúscula?**
Por la misma convención: al iniciar con minúscula, ANTLR las identifica como reglas del parser, que son las que combinan tokens para formar estructuras más complejas.

**6. ¿Cuál es la función de `->skip`?**
Le indica al lexer que, aunque reconoció un patrón (como los espacios o los saltos de línea), no debe generar un token para él ni enviarlo al parser; simplemente lo descarta.

**7. ¿Qué representa EOF?**
Representa el final del archivo de entrada (End Of File). Se usa en las reglas sintácticas para asegurar que toda la entrada fue consumida y reconocida correctamente, sin que quede texto sin procesar.

**8. ¿Qué información representa un árbol sintáctico?**
Representa la estructura jerárquica de la entrada según las reglas de la gramática: los nodos internos corresponden a las reglas sintácticas aplicadas, y las hojas corresponden a los tokens reconocidos por el lexer.

**9. ¿Cuál es la diferencia entre Listener y Visitor?**
El Listener deja que ANTLR recorra el árbol de forma automática y dispara eventos (`enterX`/`exitX`) en cada nodo, sin que el programador controle el orden del recorrido. El Visitor, en cambio, da control explícito: el programador decide cuándo y cómo visitar cada nodo del árbol, lo cual resulta útil para tareas como evaluar expresiones o generar código.

**10. ¿Cómo podría utilizarse ANTLR para construir un lenguaje de dominio específico?**
Se define una gramática propia con las palabras clave, los operadores y las estructuras particulares del dominio (por ejemplo, los comandos de un sistema de ventas), y ANTLR genera el lexer y el parser que reconocen ese lenguaje. Sobre ellos se implementa después la lógica de interpretación o ejecución mediante un Listener o un Visitor.
