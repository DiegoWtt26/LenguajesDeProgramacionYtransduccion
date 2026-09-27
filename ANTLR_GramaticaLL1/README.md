# Actividad ANTLR 4 — Gramática LL(1) para operaciones aritméticas y trigonométricas

Integrantes

* Camilo Bernal
* Diego Moreno
* Yeisson Rincón

## Requisitos

Para que el proyecto funcione se necesita:

* Linux (lo hicimos en Ubuntu)
* Python 3.8 o superior
* Java 11 o superior
* ANTLR 4.13.2 (el archivo `antlr-4.13.2-complete.jar` y el comando `antlr4`)
* El runtime de ANTLR para Python, en la misma versión que ANTLR:

```
pip install antlr4-python3-runtime==4.13.2
```

* Opcional, para ver el árbol sintáctico: `pip install antlr4-tools`

![CA1](capturas/CA1.png)

## ¿De qué trata la actividad?

La actividad consiste en diseñar e implementar una gramática LL(1) para un lenguaje pequeño que permite:

* Operaciones: `+`, `-`, `*`, `/`, `%` (también `mod`) y valor absoluto con `abs(x)` o `|x|`
* Funciones trigonométricas: `sin`, `cos`, `tan` (en radianes)
* Asignación de variables, por ejemplo `x = 2 + 3 * 4;`

ANTLR se encarga de generar el analizador léxico y sintáctico a partir de la gramática, y en Python hicimos la parte semántica, el manejo de errores y el cálculo de los conjuntos de Primeros, Siguientes y Predicción. Todas las entradas se leen desde archivos.

## Estructura del proyecto

```
proyecto_ll1/
├── Calculadora.g4      gramática (parte léxica y sintáctica)
├── generated/          código que genera ANTLR
├── errores.py          errores léxicos y sintácticos
├── semantico.py        análisis semántico (Visitor)
├── main.py             programa principal
├── conjuntos.py        Primeros, Siguientes y Predicción
├── entradas/           archivos de prueba
└── capturas/           capturas de la ejecución
```

## Cómo ejecutarlo

```
antlr4 -Dlanguage=Python3 -visitor -no-listener -o generated Calculadora.g4
python3 main.py entradas/correcto.txt
python3 conjuntos.py Calculadora.g4
```

## Paso a paso

### 1. Gramática

En `Calculadora.g4` están las reglas léxicas (en mayúscula) y las sintácticas (en minúscula). Para que sea LL(1) no tiene recursión por la izquierda, por eso las reglas quedan como `expr : term exprP` en vez de `expr : expr + term`. Las alternativas vacías son las producciones ε.

![CA2](capturas/CA2.png)

Con ANTLR generamos el lexer, el parser y el visitor en Python:

![CA3](capturas/CA3.png)

Probamos que ANTLR reconoce el lenguaje con el archivo `entradas/prueba.txt`:

![CA4](capturas/CA4.png)

![CA5](capturas/CA5.png)

### 2. Errores léxicos y sintácticos

En `errores.py` reemplazamos los mensajes de error de ANTLR por unos en español, con línea y columna. Además los errores se guardan en una lista, y si hay alguno el programa no pasa a la parte semántica.

![CA6](capturas/CA6.png)

### 3. Análisis semántico

En `semantico.py` recorremos el árbol con un Visitor. Ahí se evalúan las expresiones, se guardan las variables en la tabla de símbolos y se detectan errores como variables no declaradas, división entre cero o módulo entre cero.

![CA7](capturas/CA7.png)

### 4. Programa principal

`main.py` recibe el archivo de entrada y ejecuta las tres fases en orden: léxica, sintáctica y semántica.

![CA8](capturas/CA8.png)

### 5. Pruebas

Programa correcto con todas las operaciones:

![CA9](capturas/CA9.png)

Error léxico (caracteres que no pertenecen al lenguaje):

![CA10](capturas/CA10.png)

Errores sintácticos (falta `;`, falta `)` y operador sin operando):

![CA11](capturas/CA11.png)

Errores semánticos (variable no declarada, división y módulo entre cero):

![CA12](capturas/CA12.png)

### 6. Conjuntos de Primeros, Siguientes y Predicción

`conjuntos.py` lee la gramática directamente del archivo `Calculadora.g4`, calcula los tres conjuntos y revisa que los conjuntos de predicción de cada no terminal no tengan elementos en común, que es la condición para que la gramática sea LL(1).

![CA13](capturas/CA13.png)
