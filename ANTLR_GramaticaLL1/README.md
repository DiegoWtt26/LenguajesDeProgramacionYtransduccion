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

<p align="center"><img src="capturas/CA1.png" alt="CA1"></p>

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
├── errores.py          errores léxicos y sintácticos
├── semantico.py        análisis semántico (Visitor)
├── main.py             programa principal
├── conjuntos.py        Primeros, Siguientes y Predicción
├── entradas/           archivos de prueba
└── capturas/           capturas de la ejecución
```

## Cómo ejecutarlo

```
python3 main.py entradas/correcto.txt
python3 conjuntos.py Calculadora.g4
```

## Paso a paso

### 1. Gramática

En `Calculadora.g4` están las reglas léxicas (en mayúscula) y las sintácticas (en minúscula). Para que sea LL(1) no tiene recursión por la izquierda, por eso las reglas quedan como `expr : term exprP` en vez de `expr : expr + term`. Las alternativas vacías son las producciones ε.

<p align="center"><img src="capturas/CA2.png" alt="CA2"></p>

Con ANTLR generamos el lexer, el parser y el visitor en Python:

<p align="center"><img src="capturas/CA3.png" alt="CA3"></p>

Probamos que ANTLR reconoce el lenguaje con el archivo `entradas/prueba.txt`:

<p align="center"><img src="capturas/CA4.png" alt="CA4"></p>

<p align="center"><img src="capturas/CA5.png" alt="CA5"></p>

### 2. Errores léxicos y sintácticos

En `errores.py` reemplazamos los mensajes de error de ANTLR por unos en español, con línea y columna. Además los errores se guardan en una lista, y si hay alguno el programa no pasa a la parte semántica.

<p align="center"><img src="capturas/CA6.png" alt="CA6"></p>

### 3. Análisis semántico

En `semantico.py` recorremos el árbol con un Visitor. Ahí se evalúan las expresiones, se guardan las variables en la tabla de símbolos y se detectan errores como variables no declaradas, división entre cero o módulo entre cero.

<p align="center"><img src="capturas/CA7.png" alt="CA7"></p>

### 4. Programa principal

`main.py` recibe el archivo de entrada y ejecuta las tres fases en orden: léxica, sintáctica y semántica.

<p align="center"><img src="capturas/CA8.png" alt="CA8"></p>

### 5. Pruebas

Programa correcto con todas las operaciones:

<p align="center"><img src="capturas/CA9.png" alt="CA9"></p>

Error léxico (caracteres que no pertenecen al lenguaje):

<p align="center"><img src="capturas/CA10.png" alt="CA10"></p>

Errores sintácticos (falta `;`, falta `)` y operador sin operando):

<p align="center"><img src="capturas/CA11.png" alt="CA11"></p>

Errores semánticos (variable no declarada, división y módulo entre cero):

<p align="center"><img src="capturas/CA12.png" alt="CA12"></p>

### 6. Conjuntos de Primeros, Siguientes y Predicción

`conjuntos.py` lee la gramática directamente del archivo `Calculadora.g4`, calcula los tres conjuntos y revisa que los conjuntos de predicción de cada no terminal no tengan elementos en común, que es la condición para que la gramática sea LL(1).

<p align="center"><img src="capturas/CA13.png" alt="CA13"></p>
