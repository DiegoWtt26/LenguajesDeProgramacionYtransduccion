# Actividad ANTLR 4 — Lenguaje de instrucciones

## Integrantes

- Camilo Bernal
- Diego Moreno
- Yeisson Rincon

## Descripción

Lenguaje simple en ANTLR 4 para instrucciones del tipo:
`mostrar ventas`, `cargar clientes`, `graficar ingresos`.

## Gramática

Contenido de `Instruccion.g4`:

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

## Reglas léxicas

- **MOSTRAR, CARGAR, GRAFICAR**: palabras clave `mostrar`, `cargar`, `graficar`. Mayúscula inicial por convención ANTLR para tokens.
- **ID**: uno o más caracteres alfabéticos (`[a-zA-Z]+`). Nombres de cada instrucción (ventas, clientes, ingresos...).
- **WS**: espacios, tabulaciones y saltos de línea, con `-> skip` para descarte en el lexer.

## Reglas sintácticas

- **programa**: regla inicial. Una o más instrucciones (`instruccion+`) + fin de archivo (`EOF`). Varias instrucciones por archivo de entrada.
- **instruccion**: palabra clave (`MOSTRAR`, `CARGAR` o `GRAFICAR`) + identificador (`ID`).

## Tokens reconocidos

Entrada: `pruebas_validas.txt` (5 pruebas)

```
grun Instruccion programa -tokens pruebas_validas.txt
```

![Tokens reconocidos](tokens.png)

## Árbol sintáctico

```
grun Instruccion programa -tree pruebas_validas.txt
```

![Árbol sintáctico en texto](arbol_texto.png)

![Árbol sintáctico gráfico](arbol_grafico.png)

## Casos de error

**Error 1** — orden incorrecto (`error1.txt`: `ventas mostrar`)

![Error 1](error1.png)

**Error 2** — instrucción incompleta (`error2.txt`: `graficar`, sin ID)

![Error 2](error2.png)

**Error 3** — palabra fuera de gramática (`error3.txt`: `eliminar ventas`)

![Error 3](error3.png)

## Lexer y parser

Lexer: trabajo sobre caracteres. Agrupación del texto en tokens (palabras clave, identificadores) y descarte de espacios.

Parser: trabajo sobre tokens. Verificación del orden según las reglas sintácticas y construcción del árbol.

Uno define "qué es cada parte", el otro "si el orden es válido". Etapas separadas, diseño y depuración por separado. Base de compiladores e intérpretes.

## Preguntas de análisis

**1. ¿Diferencia entre lexema y token?**
Lexema: secuencia tal cual en la entrada (`mostrar`). Token: categoría asignada (`MOSTRAR`). Un token como `ID` agrupa varios lexemas (`ventas`, `clientes`...).

**2. ¿Responsabilidad del lexer?**
Conversión de caracteres a tokens. Agrupación y descarte de espacios.

**3. ¿Responsabilidad del parser?**
Verificación de la secuencia de tokens según la gramática. Construcción del árbol sintáctico.

**4. ¿Por qué las léxicas en mayúscula?**
Convención ANTLR para distinguir tokens de reglas sintácticas en el mismo archivo.

**5. ¿Por qué las sintácticas en minúscula?**
La otra mitad de la convención: minúscula = regla del parser, combinación de tokens.

**6. ¿Función de `->skip`?**
Descarte en el lexer. Reconocimiento sin generación de token ni envío al parser.

**7. ¿Qué es EOF?**
Fin de archivo. Control de consumo total de la entrada, sin texto restante.

**8. ¿Qué representa el árbol sintáctico?**
Estructura jerárquica según la gramática. Nodos internos = reglas aplicadas, hojas = tokens.

**9. ¿Listener frente a Visitor?**
Listener: recorrido automático con eventos (`enterX`/`exitX`), sin control del orden. Visitor: visita explícita por código propio, control total. Útil en evaluación o generación.

**10. ¿Uso de ANTLR para un DSL?**
Definición de gramática con palabras y estructuras del dominio, generación de lexer/parser, e implementación de la lógica con Listener o Visitor.
