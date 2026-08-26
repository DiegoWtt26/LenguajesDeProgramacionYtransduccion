# Calculadora Científica Graficadora con ANTLR (Patrón Visitor)

Actividad práctica del curso **Lenguajes de Programación y Traducción**.
Tema: ANTLR 4, árboles sintácticos y patrón de diseño Visitor.

## Integrantes
- Camilo Bernal
- Diego Moreno
- Yeisson Rincón

## Descripción

Se construyó progresivamente un pequeño lenguaje matemático (DSL) usando ANTLR 4,
partiendo de una calculadora aritmética básica hasta llegar a una calculadora
científica con variables, funciones matemáticas, constantes, comandos de utilidad
y graficación de funciones.

## Entorno usado

- Java: OpenJDK 21 (JDK)
- ANTLR: 4.13.2 (`antlr-4.13.2-complete.jar`, vía `$CLASSPATH`)
- SO: Linux (Ubuntu)

## Estructura de esta carpeta

~~~
ScientificCalculator/
├── README.md
├── .gitignore
├── capturas/
│   └── pasoN.png              # Evidencia de cada paso del tutorial
├── ScientificCalc.g4          # Gramática (código fuente principal)
├── Main.java                  # Programa principal
├── ScientificEvalVisitor.java # Implementación del patrón Visitor
├── PlotWindow.java            # Ventana Swing para graficar funciones
└── ejemplos.txt               # Archivo de pruebas
~~~

> Los archivos generados automáticamente por ANTLR (`ScientificCalcLexer.java`,
> `ScientificCalcParser.java`, `ScientificCalcVisitor.java`,
> `ScientificCalcBaseVisitor.java`, `*.tokens`, `*.interp`) no se versionan
> (ver `.gitignore`): se regeneran con el comando de la siguiente sección.

## Cómo ejecutar

~~~bash
antlr4 -no-listener -visitor ScientificCalc.g4
javac *.java
java Main
~~~

Luego se escriben expresiones línea por línea, por ejemplo:

~~~
2+2
radio = 10
area = pi * radio^2
area
plot(sin(x), -6.28, 6.28)
~~~

---

## Recorrido del laboratorio, paso a paso

Cada sección corresponde a la numeración del documento guía. Se indica si la
sección fue **práctica** (código + comprobación en terminal, con captura) o de
**análisis** (respuesta conceptual, sin comprobación en terminal).

### Sección 3 — Recordando la calculadora del libro (análisis)
Se repasó cómo las etiquetas (`# MulDiv`, `# AddSub`, etc.) de una regla de ANTLR
generan métodos `visit` distintos en el Visitor, evitando un único método con
condicionales para decidir el tipo de nodo. Cada nodo llega ya clasificado a su
propio método, con su `Context` tipado (ej. `AddSubContext` da acceso directo a
`.op`, `.expr(0)`, `.expr(1)`).

### Sección 4 — Crear el proyecto (práctica)
Se creó la carpeta `ScientificCalculator/` con los archivos base.

### Sección 5 — Nuestra primera gramática (práctica)
Se escribió `ScientificCalc.g4` con las reglas `prog`, `stat` y `expr` para una
calculadora aritmética básica.

### Sección 6 — ¿Qué reconoce esta gramática? (práctica + hazlo tú)
Se generó el lexer y se probó con `grun ScientificCalc prog -tokens` si distintos
textos son reconocidos como un solo `ID`:

| Texto | Resultado | ¿Un solo ID? |
|---|---|---|
| `variable` | `ID` | Sí |
| `x2` | `ID` | Sí |
| `2x` | `NUMBER` + `ID` | No |
| `_resultado` | `ID` | Sí |
| `variable-final` | `ID` + `'-'` + `ID` | No |

**Conclusión:** la regla `ID: [a-zA-Z_][a-zA-Z_0-9]*` exige que el primer carácter
sea letra o `_`; el guion `-` nunca es parte de un identificador.
Captura: `capturas/paso6.png`

### Sección 7 — Generar el Visitor (práctica + análisis)
Se ejecutó `antlr4 -no-listener -visitor ScientificCalc.g4` y se confirmó con
`grep "visit" ScientificCalcVisitor.java` que se generaron los métodos por cada
etiqueta de la gramática (`visitPrintExpr`, `visitAssign`, `visitAddSub`, etc.).

### Sección 8 — Crear nuestro Visitor (práctica)
Se creó `ScientificEvalVisitor.java` extendiendo `ScientificCalcBaseVisitor<Double>`,
con un `Map<String, Double> memory` como tabla de símbolos.

### Sección 9 — Interpretar números (práctica)
Se implementó `visitNumber`, convirtiendo el texto del token `NUMBER` a `double`.
Captura: `capturas/paso9.png`

### Sección 10 — Implementar suma y resta (práctica + hazlo tú)
Se implementó `visitAddSub`.
Captura: `capturas/paso10.png`

**Ahora hazlo tú:** se implementó `visitMulDiv` con el mismo patrón, comparando
`ctx.op.getType()` contra `MUL`/`DIV`.
Captura: `capturas/paso10b.png`

### Sección 11 — Paréntesis (práctica)
Se implementó `visitParens`, delegando en `visit(ctx.expr())`.
Captura: `capturas/paso11.png`

### Sección 12 — Construir el programa principal (práctica)
Se creó `Main.java`: lexer -> CommonTokenStream -> parser -> árbol -> visitor.
Captura: `capturas/paso12.png`

### Sección 13 — Mostrar los resultados (práctica)
Se implementó `visitPrintExpr`.
Captura: `capturas/paso13.png`

### Sección 14 — Primera prueba del intérprete (práctica)
Se probó `2+2`, `10-3`, `10*5`, `20/4`, `2+3*4`, `(2+3)*4`, confirmando que se
respeta la precedencia de operadores.
Captura: `capturas/paso14.png`

### Sección 15 — Incorporar variables (práctica)
Se implementaron `visitAssign` y `visitId`.
Captura: `capturas/paso15.png`

### Sección 16 — Compruebe las variables (práctica + análisis)
Prueba con `a = 10`, `b = 20`, `a+b`, `a*b`.
Captura: `capturas/paso16.png`

**Detente y analiza:** usar una variable no definida imprime un aviso por
`System.err` y devuelve `0.0` en vez de detener la ejecución — decisión de
diseño más "amigable" pero que puede ocultar errores del usuario.

### Sección 17 — Agregar potencia (práctica)
Se agregó `<assoc=right> expr '^' expr # power` y se implementó `visitPower`.
Capturas: `capturas/paso17.png`, `capturas/paso17.5.png`

### Sección 18 — Compruebe la potencia (práctica + hazlo tú)
Se calcularon a mano los resultados esperados antes de ejecutar
(`2^8=256`, `10^2=100`, `2^3+4=12`, `2*3^2=18`) y se confirmaron.
Captura: `capturas/paso18.png`

### Sección 19-20 — Funciones matemáticas (práctica)
Se agregó la regla `function` y `visitFunctionCall` con un `switch` sobre `Math`.
Capturas: `capturas/paso19.png`, `capturas/paso20.png`

### Sección 21 — Pruebe las funciones (práctica)
`sqrt(25)`, `cos(0)`, `log(100)` funcionan; `abs(-10)` falla como anticipa el
tutorial, por no soportar aún números negativos.
Captura: `capturas/paso21.png`

### Sección 22 — Operadores unarios (práctica)
Se agregó `op=('+'|'-') expr # unary` y `visitUnary`.
Capturas: `capturas/paso22.png`, `capturas/paso22.2.png`, `capturas/paso22.3.png`

### Sección 23 — Constantes matemáticas (práctica)
Se agregó la regla `constant` (`pi`, `e`) y `visitConstantExpr`.
Capturas: `capturas/paso23.png`, `capturas/paso23.2.png`

### Sección 24 — Primera calculadora científica (práctica)
Prueba integral: `pi`, `2*pi`, `sin(pi/2)`, `cos(0)`, `log(100)`, `ln(e)`,
`sqrt(25)`, `2^8`.
Captura: `capturas/paso24.png`

### Sección 25 — Comando clear (práctica)
Se agregó `visitClear`, que vacía `memory`.
Capturas: `capturas/paso25.png`, `capturas/paso25.2.png`

### Sección 26 — Comando vars (práctica)
Se agregó `visitShowVars`, que recorre `memory` e imprime cada variable.
Capturas: `capturas/paso26.png`, `capturas/paso26.2.png`

### Sección 27-30 — Diseño de la graficación (análisis)
Se explicó la estrategia de muestreo: reutilizar el mismo árbol sintáctico
muchas veces, cambiando `x` en `memory` antes de cada `visit`. Se diseñó la
sintaxis `plot(expr, xmin, xmax)`.
Captura: `capturas/paso28.png`

### Sección 31 — Implemente visitPlotExpr (práctica)
Se implementó `visitPlotExpr`: 800 muestras entre `xmin` y `xmax`, reasignando
`x` en `memory` y revisitando `ctx.expr(0)` en cada iteración.
Captura: `capturas/paso31.png`

### Sección 32 — Un problema interesante (análisis + hazlo tú)
Expresiones como `1/x` producen `Infinity`/`NaN` en discontinuidades. Se
filtraron con `Double.isFinite(y)` antes de agregar los puntos a las listas.

### Sección 33 — Crear la ventana gráfica (práctica)
Se creó `PlotWindow.java`, un `JPanel` embebido en un `JFrame` (800x600).
Captura: `capturas/paso33.png`

### Sección 34-36 — ymin/ymax, transformar coordenadas, dibujar (práctica)
Se implementó `paintComponent`: cálculo de límites con streams, transformación
a coordenadas de píxel (invirtiendo el eje Y) y dibujo con `drawLine`.
Captura: `capturas/paso34-36.png`

### Sección 37 — Primera gráfica (práctica)
Se ejecutó `plot(x^2,-10,10)` (parábola) y `plot(sin(x),-6.28,6.28)` (seno).
Capturas: `capturas/paso37.png`, `capturas/paso37.2.png`

### Sección 38 — Archivo de pruebas (práctica)
Se creó `ejemplos.txt` y se ejecutó con `java Main < ejemplos.txt`.
Captura: `capturas/paso38.png`

### Sección 39 — Explore el árbol sintáctico (análisis)
Para `sin(x) + 2*x^2` se identificó cada parte del árbol: suma (raíz),
función seno, multiplicación, potencia, identificador `x` (dos veces) y
número `2`. `visit(ctx.expr())` visita una estructura de árbol, no texto.

### Sección 40 — Compruebe todo el lenguaje (práctica)
Prueba integral final combinando variables, funciones, `vars` y `plot`.
Captura: `capturas/paso40.png`

### Sección 41 — Preguntas finales (análisis)

1. **Lexer:** convierte el texto crudo en tokens.
2. **Parser:** organiza los tokens en un árbol sintáctico según la gramática.
3. **Etiquetas:** generan un tipo de nodo distinto por alternativa, habilitando
   un método `visit` específico por caso.
4. **Ventaja del Visitor:** separa sintaxis de semántica, permitiendo extender
   el lenguaje sin acoplar lógica de negocio a la gramática.
5. **Tabla de símbolos:** el mapa `memory`.
6. **Por qué cambia x al graficar:** se reasigna en cada muestra para trazar
   la curva `y=f(x)`.
7. **Por qué se puede evaluar el mismo árbol varias veces:** el árbol es
   estático; solo cambia el estado externo (`memory`).
8. **Discontinuidad al graficar:** produce `NaN`/`Infinity`, filtrado con
   `Double.isFinite(y)`.
9. **Funciones con dos argumentos:** requeriría una regla de gramática con
   lista de expresiones separadas por comas.
10. **Por qué es un DSL:** el lenguaje se diseñó específicamente para cálculo
    matemático y graficación, no para propósito general.

### Sección 42 — Retos (opcional, no realizados)

### Sección 43 — Lista de comprobación (análisis)
Todos los ítems del checklist fueron implementados y comprobados.

### Sección 44 — Reflexión final (análisis)
El laboratorio mostró que separar la gramática (sintaxis) del Visitor
(semántica) permite construir un lenguaje de forma incremental. Esta
arquitectura -- Gramática -> Lexer -> Parser -> Árbol -> Visitor -- es la base
de intérpretes, compiladores y lenguajes de dominio específico (DSL).
