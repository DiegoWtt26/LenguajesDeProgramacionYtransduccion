# Calculadora Científica Graficadora con ANTLR (Patrón Visitor)

Actividad práctica del curso **Lenguajes de Programación y Traducción**.
Tema: ANTLR 4, árboles sintácticos y patrón de diseño Visitor.

## Integrantes

- Camilo Bernal
- Diego Moreno
- Yeisson Rincón

## Descripción general

Este proyecto construye, de forma incremental, un pequeño lenguaje de dominio específico (DSL) para cálculo matemático usando **ANTLR 4**. Se parte de una calculadora aritmética muy simple (suma, resta, multiplicación, división) y se va extendiendo paso a paso hasta obtener una calculadora científica capaz de:

- Evaluar expresiones matemáticas con precedencia de operadores correcta.
- Almacenar y reutilizar variables (tabla de símbolos).
- Calcular potencias, usar operadores unarios y funciones científicas (`sin`, `cos`, `tan`, `sqrt`, `log`, `ln`, `abs`, `exp`, `asin`, `acos`, `atan`, `floor`, `ceil`).
- Usar funciones de dos argumentos (`pow`, `max`, `min`).
- Usar constantes matemáticas (`pi`, `e`).
- Ejecutar comandos de utilidad (`clear`, `vars`).
- **Graficar funciones** en una ventana Swing, con rango vertical opcional y soporte para varias funciones en la misma gráfica.
- **Definir funciones propias del usuario** (`f(x) = x^2 + 2*x + 1`) y usarlas como cualquier otra función, incluso dentro de `plot`.

La arquitectura general de todo el intérprete es siempre la misma, sin importar cuánto crezca el lenguaje:

~~~
Entrada de texto  -->  Lexer  -->  Tokens  -->  Parser  -->  Árbol sintáctico  -->  Visitor  -->  Resultado
~~~

- El **Lexer** convierte el texto crudo en una secuencia de tokens (números, identificadores, operadores, palabras clave).
- El **Parser** organiza esos tokens en un árbol sintáctico, siguiendo las reglas que se definieron en la gramática.
- El **Visitor** recorre ese árbol y le da significado a cada nodo (esto es lo que realmente "ejecuta" el lenguaje).

La idea central de todo el laboratorio es entender que **la gramática define la sintaxis** (qué combinaciones de símbolos son válidas) y **el Visitor define la semántica** (qué significa cada combinación válida). Esta separación es la misma que usan los compiladores, intérpretes y traductores reales.

## Entorno usado

- Java: OpenJDK 21 (JDK, no solo JRE — se necesita `javac`)
- ANTLR: 4.13.2 (`antlr-4.13.2-complete.jar`, agregado al `$CLASSPATH` del sistema)
- Sistema operativo: Linux (Ubuntu)

## Estructura de esta carpeta

~~~
ScientificCalculator/
├── README.md
├── .gitignore
├── capturas/
│   ├── pasoN.png                    Evidencia de cada paso del laboratorio base
│   └── retoN.png                    Evidencia de los 5 retos opcionales
├── ScientificCalc.g4                Gramática ANTLR (código fuente principal)
├── Main.java                        Programa principal (arma el pipeline lexer-parser-visitor)
├── ScientificEvalVisitor.java       Implementación del patrón Visitor (la semántica del lenguaje)
├── PlotWindow.java                  Ventana Swing que dibuja la(s) función(es) graficada(s)
└── ejemplos.txt                     Archivo de prueba con instrucciones de ejemplo
~~~

Los archivos que ANTLR genera automáticamente a partir de `ScientificCalc.g4` (`ScientificCalcLexer.java`, `ScientificCalcParser.java`, `ScientificCalcVisitor.java`, `ScientificCalcBaseVisitor.java`, y los `*.tokens`/`*.interp`) **no se suben al repositorio**. No son código escrito por el equipo, son un derivado reproducible del `.g4`, y por convención en cualquier proyecto que usa un generador de código (ANTLR, protobuf, etc.) solo se versiona la fuente real, no lo generado. Por eso están listados en `.gitignore`.

## Instrucciones para descargar y ejecutar el proyecto

A continuación se detallan, paso a paso, los comandos exactos que debe correr cualquier persona que quiera descargar y probar este proyecto desde cero, sin conocimiento previo del repositorio.

### 1. Requisitos previos

- **Java JDK** 11 o superior instalado (no solo el JRE, porque se necesita el compilador `javac`). Se puede verificar con:
  ~~~bash
  javac -version
  ~~~
- **ANTLR 4** instalado y accesible como comando `antlr4` desde la terminal. La forma más común de instalarlo en Linux es descargar el jar oficial y agregarlo al `CLASSPATH`, siguiendo la guía oficial de instalación de ANTLR (https://github.com/antlr/antlr4/blob/master/doc/getting-started.md). Se puede verificar con:
  ~~~bash
  antlr4
  ~~~
  (debería mostrar la ayuda de la herramienta, no un error de "comando no encontrado").

### 2. Clonar el repositorio

~~~bash
git clone https://github.com/DiegoWtt26/LenguajesDeProgramacionYtransduccion.git
~~~

### 3. Entrar a la carpeta de esta actividad

~~~bash
cd LenguajesDeProgramacionYtransduccion/ScientificCalculator
~~~

### 4. Generar el lexer, el parser y el visitor a partir de la gramática

Este paso es obligatorio siempre que se clona el repositorio por primera vez, porque estos archivos generados no vienen incluidos (ver la nota en la sección anterior):

~~~bash
antlr4 -no-listener -visitor ScientificCalc.g4
~~~

Esto crea cuatro archivos nuevos en la misma carpeta: `ScientificCalcLexer.java`, `ScientificCalcParser.java`, `ScientificCalcVisitor.java`, `ScientificCalcBaseVisitor.java`.

### 5. Compilar todo el proyecto

~~~bash
javac *.java
~~~

Esto compila tanto los archivos generados en el paso anterior como los archivos escritos a mano (`Main.java`, `ScientificEvalVisitor.java`, `PlotWindow.java`).

### 6. Ejecutar el intérprete

~~~bash
java Main
~~~

El programa queda esperando instrucciones por consola, línea por línea. Por ejemplo:

~~~
radio = 10
area = pi * radio^2
area
sin(pi/2)
plot(sin(x), -6.28, 6.28)
~~~

Para terminar la sesión, se cierra la entrada con `Ctrl+D` (Linux/Mac) o `Ctrl+Z` seguido de Enter (Windows).

### Alternativa: ejecutar el archivo de ejemplos incluido

En vez de escribir instrucciones a mano, se puede correr de una sola vez el archivo `ejemplos.txt`, que ya contiene un recorrido completo por todas las capacidades del lenguaje (incluyendo los 5 retos opcionales):

~~~bash
java Main < ejemplos.txt
~~~

---

## Recorrido del laboratorio, paso a paso

A continuación se documenta cada sección del laboratorio guía, en el mismo orden en que fue desarrollado. Cada sección indica si fue una parte **práctica** (se escribió código y se comprobó en terminal, con evidencia fotográfica) o de **análisis** (una reflexión conceptual, sin ejecución de código).

### Sección 3 — Recordando la calculadora del libro (análisis)

Antes de escribir la gramática propia, se repasó el ejemplo clásico de calculadora del libro guía, cuya regla de expresiones usa etiquetas como estas:

~~~antlr
expr
    : expr op=('*'|'/') expr # MulDiv
    | expr op=('+'|'-') expr # AddSub
    | INT                    # int
    | ID                     # id
    | '(' expr ')'           # parens
    ;
~~~

**Pregunta de análisis:** ¿por qué conviene tener un método distinto para una suma, una multiplicación y un número, en lugar de un único método genérico?

**Respuesta:** si todo cayera en un solo método `visitExpr`, ese método tendría que empezar con una cadena de `if`/`else` para descubrir manualmente si el nodo actual es una suma, una multiplicación, un número, etc. Cada etiqueta (`# MulDiv`, `# AddSub`, `# int`...) le indica a ANTLR que genere un tipo de nodo Java distinto para cada alternativa de la regla, y por lo tanto un método `visit` distinto por cada uno (`visitMulDiv`, `visitAddSub`, `visitInt`...). Esto es una aplicación del patrón Visitor: el objeto que se está recorriendo "sabe" qué tipo es, y el despacho a la implementación correcta ocurre automáticamente, sin condicionales manuales. Además, cada método recibe un `Context` ya tipado (por ejemplo `AddSubContext` expone directamente `.op`, `.expr(0)`, `.expr(1)`), lo que hace el código más simple y menos propenso a errores.

### Sección 4 — Crear el proyecto (práctica)

Se creó la carpeta `ScientificCalculator/` con la estructura inicial mínima:

~~~bash
mkdir ScientificCalculator
cd ScientificCalculator
touch ScientificCalc.g4 Main.java ScientificEvalVisitor.java PlotWindow.java ejemplos.txt
~~~

Todos los archivos que ANTLR genera a partir de la gramática (lexer, parser, visitor base) se crean automáticamente en pasos posteriores; no se escriben a mano.

### Sección 5 — Nuestra primera gramática (práctica)

Se escribió la primera versión de `ScientificCalc.g4`, con tres reglas principales:

- `prog`: el punto de entrada, una o más instrucciones (`stat`) seguidas de fin de archivo.
- `stat`: una instrucción, que puede ser imprimir una expresión, asignar una variable, o una línea en blanco.
- `expr`: una expresión aritmética, con multiplicación/división, suma/resta, números, identificadores y paréntesis.

~~~antlr
grammar ScientificCalc;

prog
    : stat+ EOF
    ;

stat
    : expr NEWLINE               # printExpr
    | ID '=' expr NEWLINE        # assign
    | NEWLINE                    # blank
    ;

expr
    : expr op=('*'|'/') expr     # mulDiv
    | expr op=('+'|'-') expr     # addSub
    | NUMBER                     # number
    | ID                         # id
    | '(' expr ')'               # parens
    ;

MUL : '*';
DIV : '/';
ADD : '+';
SUB : '-';

NUMBER : [0-9]+ ('.' [0-9]+)? ;
ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
NEWLINE: '\r'? '\n' ;
WS     : [ \t]+ -> skip ;
~~~

Un detalle importante: el orden de las alternativas en `expr` define la precedencia. ANTLR resuelve la ambigüedad de una gramática con recursión izquierda dándole mayor precedencia a las alternativas que aparecen primero, por eso `mulDiv` está antes que `addSub` — así se asegura que la multiplicación/división se evalúe antes que la suma/resta, tal como en matemáticas.

### Sección 6 — ¿Qué reconoce esta gramática? (práctica + "ahora hazlo tú")

Antes de generar el código Java, se analizó qué exactamente reconocen las reglas léxicas `NUMBER` e `ID`.

La regla `NUMBER: [0-9]+ ('.' [0-9]+)?` reconoce uno o más dígitos, opcionalmente seguidos de un punto decimal y más dígitos (`10`, `3.14`, `100.5`).

La regla `ID: [a-zA-Z_][a-zA-Z_0-9]*` reconoce identificadores que **empiezan** con una letra o guion bajo, y pueden continuar con letras, dígitos o guiones bajos.

**Ejercicio práctico:** se generó el lexer y se probó con la herramienta `grun` (TestRig de ANTLR) si distintos textos son reconocidos como un único token `ID`:

~~~bash
antlr4 -no-listener -visitor ScientificCalc.g4
echo "variable" | grun ScientificCalc prog -tokens
~~~

| Texto de entrada | Tokens producidos | ¿Un solo ID? | Explicación |
|---|---|---|---|
| `variable` | `ID("variable")` | Sí | Cumple la regla completa |
| `x2` | `ID("x2")` | Sí | El dígito va después de la letra inicial, es válido |
| `2x` | `NUMBER("2")` + `ID("x")` | No | Empieza con dígito; la regla exige letra o `_` como primer carácter |
| `_resultado` | `ID("_resultado")` | Sí | El guion bajo inicial está permitido |
| `variable-final` | `ID("variable")` + `SUB('-')` + `ID("final")` | No | El carácter `-` nunca pertenece a la clase de un identificador; se interpreta como una resta entre dos variables |

**Conclusión:** el primer carácter de un `ID` es lo único restringido a letra o `_`; el resto puede incluir dígitos. El guion nunca forma parte de un identificador porque ya está reservado como operador de resta en la gramática, por lo que su presencia dentro de lo que parece un nombre de variable rompe el identificador en varios tokens.

![Paso 6](capturas/paso6.png)

### Sección 7 — Generar el Visitor (práctica + análisis)

Se ejecutó el generador de código de ANTLR indicando explícitamente que se quiere la variante Visitor (y no Listener, que es la otra estrategia de recorrido de árboles que ofrece ANTLR):

~~~bash
antlr4 -no-listener -visitor ScientificCalc.g4
~~~

Esto produce cuatro archivos nuevos:

- `ScientificCalcLexer.java` — el analizador léxico.
- `ScientificCalcParser.java` — el analizador sintáctico.
- `ScientificCalcVisitor.java` — una interfaz con un método `visit...` por cada etiqueta de la gramática.
- `ScientificCalcBaseVisitor.java` — una implementación por defecto de esa interfaz, que simplemente visita a los hijos de cada nodo sin hacer nada más. Es la clase que se extiende para implementar la semántica real.

Se confirmó con `grep "visit" ScientificCalcVisitor.java` que aparecen exactamente los métodos correspondientes a las etiquetas de la sección 5: `visitPrintExpr`, `visitAssign`, `visitBlank`, `visitMulDiv`, `visitAddSub`, `visitNumber`, `visitId`, `visitParens` (más `visitProg`, generado automáticamente para la regla raíz).

Esto confirma en la práctica lo discutido en la sección 3: cada etiqueta de la gramática se traduce, de forma automática y mecánica, en un método de visita distinto.

### Sección 8 — Crear nuestro Visitor (práctica)

Se creó `ScientificEvalVisitor.java`, la clase que va a contener toda la implementación real del lenguaje (la semántica), extendiendo la clase generada `ScientificCalcBaseVisitor`:

~~~java
import java.util.HashMap;
import java.util.Map;

public class ScientificEvalVisitor
        extends ScientificCalcBaseVisitor<Double> {

    Map<String, Double> memory = new HashMap<>();
}
~~~

El parámetro genérico `<Double>` indica que cada método `visit...` va a devolver un valor de tipo `Double` — es decir, evaluar cualquier parte del árbol siempre produce un número real. Esta es una diferencia importante frente al ejemplo clásico del libro (que trabaja con `Integer`): al usar `double` desde el principio, la calculadora puede manejar decimales, raíces, logaritmos y trigonometría sin perder precisión ni tener que hacer conversiones de tipo más adelante.

El `Map<String, Double> memory` es la tabla de símbolos: asocia el nombre de cada variable con su valor actual. Es el único "estado" que persiste entre una expresión y la siguiente (el árbol sintáctico en sí es efímero, se descarta después de evaluar cada línea).

![Paso 9](capturas/paso9.png)

### Sección 9 — Interpretar números (práctica)

Se implementó el primer método real, `visitNumber`, que se ejecuta cada vez que el árbol contiene un nodo de tipo número:

~~~java
@Override
public Double visitNumber(
        ScientificCalcParser.NumberContext ctx) {

    return Double.parseDouble(
        ctx.NUMBER().getText()
    );
}
~~~

`ctx.NUMBER()` obtiene el token concreto que el lexer reconoció (por ejemplo, el texto `"3.1416"`), `.getText()` extrae ese texto tal cual apareció en la entrada, y `Double.parseDouble(...)` lo convierte al tipo numérico `double` de Java. Este es el caso base de toda la recursión del Visitor: en algún punto, cualquier expresión termina en un número literal.

### Sección 10 — Implementar suma y resta (práctica + "ahora hazlo tú")

Se implementó `visitAddSub`:

~~~java
@Override
public Double visitAddSub(
        ScientificCalcParser.AddSubContext ctx) {

    double left = visit(ctx.expr(0));
    double right = visit(ctx.expr(1));

    if (ctx.op.getType() == ScientificCalcParser.ADD) {
        return left + right;
    }

    return left - right;
}
~~~

Aquí aparece la idea central de todo el patrón Visitor: `visit(ctx.expr(0))` no evalúa directamente un número, sino que **vuelve a llamar al Visitor sobre el subárbol izquierdo**, sea cual sea su tipo (puede ser otro `AddSub`, un `MulDiv`, un número, una variable...). Esa llamada recursiva es la que hace que expresiones arbitrariamente anidadas, como `2 + 3 * (4 - 1)`, se evalúen correctamente sin que el código tenga que saber de antemano cuán compleja es la expresión. `ctx.op` es el token del operador capturado por la etiqueta `op=('+'|'-')` de la gramática, y `.getType()` permite comparar contra las constantes generadas (`ADD`, `SUB`) para decidir qué operación aplicar.

![Paso 10](capturas/paso10.png)

**Ahora hazlo tú:** siguiendo exactamente el mismo patrón, se implementó `visitMulDiv`, esta vez comparando contra `MUL` y `DIV`:

~~~java
@Override
public Double visitMulDiv(
        ScientificCalcParser.MulDivContext ctx) {

    double left = visit(ctx.expr(0));
    double right = visit(ctx.expr(1));

    if (ctx.op.getType() == ScientificCalcParser.MUL) {
        return left * right;
    }

    return left / right;
}
~~~

![Paso 10.2](capturas/paso10b.png)

### Sección 11 — Paréntesis (práctica)

Se implementó `visitParens`:

~~~java
@Override
public Double visitParens(
        ScientificCalcParser.ParensContext ctx) {

    return visit(ctx.expr());
}
~~~

Este método parece trivial (solo delega en la expresión interna, sin hacer ninguna operación adicional), pero es crucial: los paréntesis no cambian el *valor* de una expresión, pero sí cambian la *forma del árbol sintáctico*, y por lo tanto el orden en que se evalúan las operaciones. Por ejemplo, `2 + 3 * 4` y `(2 + 3) * 4` producen árboles distintos, y por eso dan resultados distintos (`14` vs `20`), aunque ambos usan los mismos números y operadores.

![Paso 11](capturas/paso11.png)

### Sección 12 — Construir el programa principal (práctica)

Se creó `Main.java`, que arma el pipeline completo lexer → tokens → parser → árbol → visitor:

~~~java
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class Main {

    public static void main(String[] args) throws Exception {

        CharStream input = CharStreams.fromStream(System.in);

        ScientificCalcLexer lexer = new ScientificCalcLexer(input);
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        ScientificCalcParser parser = new ScientificCalcParser(tokens);

        ParseTree tree = parser.prog();

        ScientificEvalVisitor visitor = new ScientificEvalVisitor();
        visitor.visit(tree);
    }
}
~~~

Cada línea corresponde a una etapa del pipeline: `CharStreams.fromStream(System.in)` lee los caracteres de la entrada estándar; el `Lexer` los convierte en tokens; el `CommonTokenStream` es un buffer que el parser va consumiendo; `parser.prog()` invoca la regla raíz de la gramática y devuelve la raíz del árbol sintáctico; y finalmente `visitor.visit(tree)` empieza a recorrer ese árbol, disparando en cascada todos los métodos `visit...` que se necesiten.

![Paso 12](capturas/paso12.png)

### Sección 13 — Mostrar los resultados (práctica)

Hasta este punto, el intérprete evalúa expresiones pero no muestra nada. Se implementó `visitPrintExpr`, que se dispara cada vez que una línea completa es solo una expresión (no una asignación):

~~~java
@Override
public Double visitPrintExpr(
        ScientificCalcParser.PrintExprContext ctx) {

    double value = visit(ctx.expr());
    System.out.println(value);
    return value;
}
~~~

![Paso 13](capturas/paso13.png)

### Sección 14 — Primera prueba del intérprete (práctica)

Con lo implementado hasta aquí (números, suma, resta, multiplicación, división, paréntesis, impresión), ya es posible compilar y ejecutar una calculadora aritmética funcional:

~~~bash
javac *.java
java Main
~~~

| Expresión | Resultado esperado |
|---|---|
| `2+2` | `4.0` |
| `10-3` | `7.0` |
| `10*5` | `50.0` |
| `20/4` | `5.0` |
| `2+3*4` | `14.0` |
| `(2+3)*4` | `20.0` |

El caso `2+3*4 = 14.0` (y no `20.0`) confirma que la precedencia de operadores definida en la gramática (multiplicación/división antes que suma/resta) se respeta correctamente.

![Paso 14](capturas/paso14.png)

### Sección 15 — Incorporar variables (práctica)

Se implementaron `visitAssign` (para guardar un valor en la tabla de símbolos) y `visitId` (para recuperarlo):

~~~java
@Override
public Double visitAssign(
        ScientificCalcParser.AssignContext ctx) {

    String id = ctx.ID().getText();
    double value = visit(ctx.expr());
    memory.put(id, value);
    return value;
}

@Override
public Double visitId(
        ScientificCalcParser.IdContext ctx) {

    String id = ctx.ID().getText();
    if (memory.containsKey(id)) {
        return memory.get(id);
    }
    System.err.println("Variable no definida: " + id);
    return 0.0;
}
~~~

`visitAssign` evalúa la expresión del lado derecho del `=`, y guarda el resultado en el mapa `memory` bajo el nombre del identificador. `visitId` hace lo contrario: cuando el árbol tiene un nodo identificador (por ejemplo, al usar `radio` dentro de `area = pi * radio^2`), busca ese nombre en `memory` y devuelve su valor.

![Paso 15](capturas/paso15.png)

### Sección 16 — Compruebe las variables (práctica + análisis)

Se probó:

~~~
a = 10
b = 20
a+b
a*b
~~~

obteniendo `30.0` y `200.0`, confirmando que la tabla de símbolos persiste correctamente entre líneas distintas.

![Paso 16](capturas/paso16.png)

**Detente y analiza:** ¿qué pasaría si se usa una variable que nunca fue asignada, como `resultado + 10`? Con la implementación actual, `visitId` imprime un aviso por `System.err` ("Variable no definida: resultado") pero **no detiene la ejecución**: devuelve `0.0` como valor por defecto, así que la expresión completa produciría `10.0`. Es una decisión de diseño con dos caras: por un lado, es más "amigable" porque el programa no se cae ante un error del usuario; por otro lado, puede ocultar errores reales (si alguien tipeó mal el nombre de una variable, el programa seguiría funcionando "silenciosamente" con un resultado incorrecto en vez de avisar con claridad). Una alternativa más estricta sería lanzar una excepción y detener la evaluación.

### Sección 17 — Agregar potencia (práctica)

Se extendió la gramática para reconocer el operador de potencia `^`:

~~~antlr
expr
    : <assoc=right> expr '^' expr   # power
    | expr op=('*'|'/') expr        # mulDiv
    | expr op=('+'|'-') expr        # addSub
    | NUMBER                        # number
    | ID                            # id
    | '(' expr ')'                  # parens
    ;
~~~

Dos detalles importantes de esta regla:

1. Se colocó **antes** que `mulDiv` y `addSub`, para darle mayor precedencia (la potencia se evalúa antes que la multiplicación y la suma, tal como en matemáticas: `2*3^2` es `2*9=18`, no `6^2=36`).
2. Se usó `<assoc=right>` para indicar asociatividad **derecha**. Esto importa en casos como `2^3^2`: con asociatividad derecha se interpreta como `2^(3^2) = 2^9 = 512`, que es la convención matemática estándar para la potenciación (a diferencia de suma o resta, que son naturalmente asociativas a la izquierda).

Se regeneró el proyecto y se implementó `visitPower`:

~~~java
@Override
public Double visitPower(
        ScientificCalcParser.PowerContext ctx) {

    double base = visit(ctx.expr(0));
    double exponent = visit(ctx.expr(1));

    return Math.pow(base, exponent);
}
~~~

![Paso 17](capturas/paso17.png)
![Paso 17.5](capturas/paso17.5.png)

### Sección 18 — Compruebe la potencia (práctica + "ahora hazlo tú")

Antes de ejecutar, se calcularon a mano los resultados esperados:

| Expresión | Cálculo | Resultado esperado |
|---|---|---|
| `2^8` | 2 elevado a la 8 | `256.0` |
| `10^2` | 10 elevado a la 2 | `100.0` |
| `2^3+4` | potencia antes que suma: 8+4 | `12.0` |
| `2*3^2` | potencia antes que multiplicación: 2*9 | `18.0` |

Se confirmaron ejecutando el intérprete, y los resultados coincidieron con lo calculado a mano, validando que la precedencia definida en la gramática funciona como se esperaba.

![Paso 18](capturas/paso18.png)

### Sección 19-20 — Funciones matemáticas (práctica)

Se agregó una nueva regla léxica `function`, que agrupa las palabras clave reservadas para funciones científicas, y una nueva alternativa en `expr` para reconocer una llamada a función:

~~~antlr
expr
    : <assoc=right> expr '^' expr   # power
    | expr op=('*'|'/') expr        # mulDiv
    | expr op=('+'|'-') expr        # addSub
    | function '(' expr ')'         # functionCall
    | NUMBER                        # number
    | ID                            # id
    | '(' expr ')'                  # parens
    ;

function
    : 'sin' | 'cos' | 'tan' | 'sqrt' | 'log' | 'ln' | 'abs' | 'exp'
    ;
~~~

Se implementó `visitFunctionCall`, que primero obtiene el nombre de la función invocada como texto, evalúa el argumento recursivamente, y luego usa un `switch` para llamar al método correspondiente de la clase `Math` de Java:

~~~java
@Override
public Double visitFunctionCall(
        ScientificCalcParser.FunctionCallContext ctx) {

    String function = ctx.function().getText();
    double value = visit(ctx.expr());

    switch (function) {
        case "sin":  return Math.sin(value);
        case "cos":  return Math.cos(value);
        case "tan":  return Math.tan(value);
        case "sqrt": return Math.sqrt(value);
        case "log":  return Math.log10(value);
        case "ln":   return Math.log(value);
        case "abs":  return Math.abs(value);
        case "exp":  return Math.exp(value);
        default:
            throw new RuntimeException("Funcion desconocida: " + function);
    }
}
~~~

Nótese la distinción entre `log` (logaritmo en base 10, `Math.log10`) y `ln` (logaritmo natural, base *e*, `Math.log`) — una fuente común de confusión, resuelta explícitamente con dos funciones separadas.

![Paso 19](capturas/paso19.png)
![Paso 20](capturas/paso20.png)

### Sección 21 — Pruebe las funciones (práctica)

Se probaron `sqrt(25)`, `cos(0)`, `log(100)`, todas funcionando correctamente. `abs(-10)` en cambio **falla**, tal como el propio tutorial anticipa: la gramática todavía no reconoce el signo `-` como parte de una expresión (solo como el operador binario de resta), así que `-10` como argumento de una función no se puede parsear todavía. Este problema se resuelve en la siguiente sección con los operadores unarios.

![Paso 21](capturas/paso21.png)

### Sección 22 — Operadores unarios (práctica)

Se agregó una nueva alternativa a `expr` para reconocer un signo `+` o `-` antepuesto a una expresión (en vez de entre dos expresiones, como en la resta binaria):

~~~antlr
| op=('+'|'-') expr             # unary
~~~

y se implementó `visitUnary`:

~~~java
@Override
public Double visitUnary(
        ScientificCalcParser.UnaryContext ctx) {

    double value = visit(ctx.expr());

    if (ctx.op.getText().equals("-")) {
        return -value;
    }
    return value;
}
~~~

Con esto, expresiones como `-10`, `abs(-10)` y `-2+5` ya se interpretan correctamente: el `-` inicial ya no se confunde con una resta binaria, sino que se reconoce como la negación de la expresión que le sigue.

![Paso 22](capturas/paso22.png)
![Paso 22.2](capturas/paso22.2.png)
![Paso 22.3](capturas/paso22.3.png)

### Sección 23 — Constantes matemáticas (práctica)

Se agregó una regla léxica `constant` para `pi` y `e`, y una alternativa `constantExpr` en `expr`:

~~~antlr
| constant                      # constantExpr

constant
    : 'pi' | 'e'
    ;
~~~

Se implementó `visitConstantExpr`:

~~~java
@Override
public Double visitConstantExpr(
        ScientificCalcParser.ConstantExprContext ctx) {

    String constant = ctx.constant().getText();

    if (constant.equals("pi")) {
        return Math.PI;
    }
    if (constant.equals("e")) {
        return Math.E;
    }
    return 0.0;
}
~~~

A diferencia de las variables (que se guardan en `memory` y el usuario puede sobrescribir), `pi` y `e` son constantes fijas del lenguaje: siempre devuelven el mismo valor, sin necesidad de que el usuario las defina primero.

![Paso 23](capturas/paso23.png)
![Paso 23.2](capturas/paso23.2.png)

### Sección 24 — Primera calculadora científica (práctica)

Con todo lo implementado hasta este punto, se hizo una prueba integral combinando potencias, funciones y constantes:

| Expresión | Resultado aproximado |
|---|---|
| `sin(pi/2)` | `1.0` |
| `cos(0)` | `1.0` |
| `log(100)` | `2.0` |
| `ln(e)` | `1.0` |
| `sqrt(25)` | `5.0` |
| `2^8` | `256.0` |

Todos los resultados coincidieron con lo esperado, confirmando que el lenguaje ya funciona como una calculadora científica completa (sin contar todavía variables persistentes complejas ni graficación).

![Paso 24](capturas/paso24.png)

### Sección 25 — Comando `clear` (práctica)

Se agregó una nueva instrucción (no una expresión, sino un comando) a la regla `stat`:

~~~antlr
| 'clear' NEWLINE            # clear
~~~

e implementado `visitClear`:

~~~java
@Override
public Double visitClear(
        ScientificCalcParser.ClearContext ctx) {

    memory.clear();
    System.out.println("Memoria eliminada.");
    return 0.0;
}
~~~

Esto demuestra que el lenguaje no está limitado a expresiones matemáticas: también puede tener comandos imperativos que actúan sobre el estado del intérprete (en este caso, vaciando la tabla de símbolos).

![Paso 25](capturas/paso25.png)
![Paso 25.2](capturas/paso25.2.png)

### Sección 26 — Comando `vars` (práctica)

De forma análoga, se agregó el comando `vars`, que lista todas las variables actualmente definidas:

~~~antlr
| 'vars' NEWLINE             # showVars
~~~

~~~java
@Override
public Double visitShowVars(
        ScientificCalcParser.ShowVarsContext ctx) {

    if (memory.isEmpty()) {
        System.out.println("No hay variables definidas.");
        return 0.0;
    }

    for (Map.Entry<String, Double> entry : memory.entrySet()) {
        System.out.println(entry.getKey() + " = " + entry.getValue());
    }
    return 0.0;
}
~~~

![Paso 26](capturas/paso26.png)
![Paso 26.2](capturas/paso26.2.png)

### Sección 27-30 — Diseño de la graficación (análisis)

Antes de programar la graficación, se analizó el problema conceptualmente. Hasta este punto, cada expresión se evalúa **una sola vez** (por ejemplo, `sin(pi/2)` produce un único número). Pero graficar una función como `y = sin(x)` requiere evaluar esa misma expresión **muchas veces**, cada vez con un valor distinto de `x`:

| x | sin(x) |
|---|---|
| -2 | -0.909 |
| -1 | -0.841 |
| 0 | 0 |
| 1 | 0.841 |
| 2 | 0.909 |

La estrategia adoptada es: asignar un valor a `x` en la tabla de símbolos, volver a visitar el mismo árbol sintáctico (que representa la expresión a graficar, por ejemplo `sin(x)`), obtener `y`, cambiar `x` a un nuevo valor, y repetir. Esto es posible precisamente porque el árbol sintáctico es una estructura estática — no cambia entre evaluaciones, solo cambia el estado externo (`memory`) que el Visitor consulta al procesar cada nodo `id`.

Se diseñó la sintaxis del comando de graficación como `plot(expresion, xmin, xmax)`, por ejemplo `plot(sin(x), -6.28, 6.28)`, y se agregó a la gramática:

~~~antlr
| 'plot' '(' expr ',' expr ',' expr ')' NEWLINE  # plotExpr
~~~

En esta regla, `ctx.expr(0)` corresponde a la expresión a graficar, `ctx.expr(1)` a `xmin`, y `ctx.expr(2)` a `xmax`.

![Paso 28](capturas/paso28.png)

### Sección 31 — Implemente `visitPlotExpr` (práctica)

Se implementó el muestreo de la función: se generan 800 puntos equiespaciados entre `xmin` y `xmax`, y para cada uno se reasigna `x` en la tabla de símbolos y se vuelve a evaluar la expresión:

~~~java
@Override
public Double visitPlotExpr(
        ScientificCalcParser.PlotExprContext ctx) {

    double xmin = visit(ctx.expr(1));
    double xmax = visit(ctx.expr(2));

    int samples = 800;

    List<Double> xs = new ArrayList<>();
    List<Double> ys = new ArrayList<>();

    for (int i = 0; i < samples; i++) {
        double x = xmin + i * (xmax - xmin) / (samples - 1);
        memory.put("x", x);
        double y = visit(ctx.expr(0));

        if (Double.isFinite(y)) {
            xs.add(x);
            ys.add(y);
        }
    }

    new PlotWindow(xs, ys);
    return 0.0;
}
~~~

*(Nota: esta versión inicial fue posteriormente reemplazada por una más completa al implementar los retos 3 y 4, ver más adelante.)*

### Sección 32 — Un problema interesante (análisis + "ahora hazlo tú")

Se identificó que expresiones como `plot(1/x, -5, 5)` producen valores especiales de Java (`Infinity`, `-Infinity`, `NaN`) cuando `x` pasa por una discontinuidad (en este caso, `x = 0`). A diferencia de la división entre enteros, dividir un `double` entre cero **no lanza una excepción**: simplemente produce estos valores especiales.

El ejercicio propuesto era filtrar esos valores antes de agregarlos a las listas de muestreo, usando `Double.isFinite(y)`. Esa condición ya está integrada directamente en el bucle de `visitPlotExpr` mostrado arriba: si `y` no es un número finito, ese punto simplemente se descarta y no se agrega a `xs`/`ys`. El efecto práctico es que la gráfica de una función con una asíntota vertical no intenta dibujar una línea infinita en ese punto: la curva simplemente se corta a cada lado de la discontinuidad.

### Sección 33 — Crear la ventana gráfica (práctica)

Se creó `PlotWindow.java`, una clase que extiende `JPanel` (de la librería gráfica Swing de Java) y que se embebe dentro de un `JFrame` (la ventana propiamente dicha):

~~~java
public class PlotWindow extends JPanel {

    private List<Double> xs;
    private List<Double> ys;

    public PlotWindow(List<Double> xs, List<Double> ys) {
        this.xs = xs;
        this.ys = ys;

        JFrame frame = new JFrame("Scientific Calculator");
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.setSize(800, 600);
        frame.add(this);
        frame.setVisible(true);
    }
}
~~~

En este punto todavía no se dibuja nada visible; solo se abre una ventana vacía de 800x600 píxeles. El dibujo real se agrega en las secciones siguientes, sobrescribiendo el método `paintComponent`.

*(Nota: esta clase fue posteriormente ampliada al implementar los retos 3 y 4, ver más adelante.)*

![Paso 33](capturas/paso33.png)

### Sección 34-36 — Encontrar ymin/ymax, transformar coordenadas y dibujar la función (práctica)

Estas tres partes se implementan juntas dentro de un único método `paintComponent`, que Swing invoca automáticamente cada vez que necesita redibujar el panel.

**Encontrar los límites verticales:** mientras `xmin`/`xmax` vienen directamente del comando `plot`, los límites verticales (`ymin`/`ymax`) se calculan automáticamente a partir de los valores obtenidos en el muestreo, usando streams de Java:

~~~java
double ymin = ys.stream().mapToDouble(Double::doubleValue).min().orElse(-1);
double ymax = ys.stream().mapToDouble(Double::doubleValue).max().orElse(1);
~~~

**Transformar coordenadas:** los datos están en el sistema de coordenadas "matemático" (por ejemplo, `x` entre -10 y 10), pero deben dibujarse en el sistema de coordenadas "de píxeles" de la ventana (por ejemplo, entre 0 y 800). Esto requiere una transformación lineal por cada eje:

~~~java
int px = (int)((x - xmin) / (xmax - xmin) * getWidth());
int py = getHeight() - (int)((y - ymin) / (ymax - ymin) * getHeight());
~~~

El signo restado en `py` (`getHeight() - ...`) es necesario porque en los sistemas de coordenadas gráficas de Java (como en la mayoría de librerías gráficas), el eje Y crece **hacia abajo** (el píxel `(0,0)` está en la esquina superior izquierda), mientras que en matemáticas el eje Y crece hacia arriba. Sin esa inversión, la gráfica saldría "al revés" (volteada verticalmente).

**Dibujar:** finalmente, se recorren los puntos consecutivos de la lista, transformando cada uno a coordenadas de píxel y dibujando un segmento de línea entre puntos consecutivos con `g2.drawLine(...)`, lo que produce visualmente una curva continua.

![Paso 34-36](capturas/paso34-36.png)

### Sección 37 — Primera gráfica (práctica)

Con todo lo anterior compilado, se ejecutó:

~~~
plot(x^2,-10,10)
~~~

obteniendo una ventana con una parábola dibujada correctamente. Se probó también:

~~~
plot(sin(x),-6.28,6.28)
~~~

confirmando la curva del seno en el rango de aproximadamente un ciclo completo (2π).

![Paso 37](capturas/paso37.png)
![Paso 37.2](capturas/paso37.2.png)

### Sección 38 — Archivo de pruebas (práctica)

Se creó `ejemplos.txt` con un conjunto representativo de instrucciones que ejercitan todas las capacidades del lenguaje (aritmética, variables, funciones, constantes, `vars`, `plot`), y se ejecutó de una sola vez redirigiendo el archivo como entrada estándar:

~~~bash
java Main < ejemplos.txt
~~~

![Paso 38](capturas/paso38.png)

### Sección 39 — Explore el árbol sintáctico (análisis)

Para la expresión `sin(x) + 2*x^2`, se identificó a qué parte del árbol corresponde cada elemento:

- **Suma:** nodo raíz, regla `addSub`, que combina el resultado de `sin(x)` con el de `2*x^2`.
- **Función seno:** un nodo `functionCall`, con `sin` como función y `x` como argumento.
- **Multiplicación:** un nodo `mulDiv` entre `2` y `x^2`.
- **Potencia:** un nodo `power` entre `x` y `2`.
- **Identificador `x`:** aparece dos veces en el árbol como nodo `id` (una vez dentro del seno, otra dentro de la potencia) — son dos nodos distintos que representan la misma variable.
- **Número `2`:** un nodo `number`.

**Detente y analiza:** cuando se ejecuta `visit(ctx.expr())`, ¿se está evaluando una cadena de texto o se está recorriendo una estructura de árbol? La respuesta es que se recorre una **estructura de árbol**: el texto original ya fue completamente convertido en objetos Java (`AddSubContext`, `FunctionCallContext`, etc.) por el lexer y el parser antes de que el Visitor entre en juego. El Visitor nunca vuelve a leer el string original; simplemente navega recursivamente por esos objetos ya construidos.

### Sección 40 — Compruebe todo el lenguaje (práctica)

Prueba de integración final, combinando todas las características implementadas:

~~~
radio = 10
area = pi * radio^2
area
angulo = pi/4
sin(angulo)
cos(angulo)
vars
plot(sin(x), -6.28, 6.28)
plot(x^2, -10, 10)
~~~

Todo el conjunto se ejecutó correctamente, confirmando que el lenguaje completo funciona de manera integrada: variables persistentes, expresiones anidadas, funciones trigonométricas, el comando `vars`, y dos gráficas distintas.

![Paso 40](capturas/paso40.png)

### Sección 41 — Preguntas finales (análisis)

1. **¿Cuál es la responsabilidad del Lexer?** Convertir el texto crudo de la entrada en una secuencia de tokens (unidades léxicas como números, identificadores, operadores y palabras clave), descartando espacios en blanco irrelevantes.

2. **¿Cuál es la responsabilidad del Parser?** Tomar la secuencia de tokens producida por el lexer y organizarla en un árbol sintáctico, verificando que la secuencia respete las reglas gramaticales definidas (y rechazando, con un error, cualquier secuencia que no las respete).

3. **¿Qué función cumplen las etiquetas como `#addSub` o `#functionCall`?** Le indican a ANTLR que genere un tipo de nodo Java distinto para cada alternativa de una regla, lo que a su vez genera un método `visit` específico para cada caso, evitando tener que distinguir manualmente los tipos de nodo dentro de un único método genérico.

4. **¿Qué ventaja ofrece el patrón Visitor?** Separa completamente la sintaxis (definida en la gramática) de la semántica (definida en la clase Visitor). Esto permite modificar o extender el significado de un lenguaje sin tocar su gramática, o extender la gramática sin necesariamente reescribir toda la lógica de evaluación existente.

5. **¿Qué representa la tabla de símbolos?** El mapa `memory`, que asocia el nombre de cada variable definida por el usuario con su valor numérico actual. Es el único estado que persiste entre la evaluación de una línea y la siguiente.

6. **¿Por qué la variable `x` cambia continuamente durante una gráfica?** Porque trazar la curva `y = f(x)` requiere conocer el valor de `y` en muchos puntos distintos de `x`; por eso, en el bucle de muestreo, `x` se reasigna en `memory` antes de cada nueva evaluación de la expresión.

7. **¿Por qué podemos evaluar el mismo árbol sintáctico varias veces?** Porque el árbol es una estructura de datos estática, construida una sola vez a partir del texto de la expresión. Lo único que cambia entre evaluaciones sucesivas es el estado externo que el Visitor consulta (la tabla de símbolos `memory`), no el árbol en sí.

8. **¿Qué sucede cuando se intenta graficar una función con una discontinuidad?** La evaluación en ese punto específico produce un valor no finito (`Infinity`, `-Infinity` o `NaN`); ese punto se filtra con `Double.isFinite(y)` antes de agregarlo a las listas de muestreo, de modo que la gráfica simplemente omite ese punto en vez de intentar dibujar un valor infinito.

9. **¿Qué modificaciones serían necesarias para implementar funciones con dos argumentos?** Habría que cambiar la regla `function '(' expr ')'` por algo que acepte una lista de expresiones separadas por comas — esto se implementó efectivamente más adelante en el reto 2 (ver sección de retos).

10. **¿Por qué la calculadora desarrollada puede considerarse un lenguaje de dominio específico (DSL)?** Porque, a diferencia de un lenguaje de propósito general (como Java o Python), este lenguaje fue diseñado exclusivamente para resolver un dominio de problemas muy acotado: cálculo matemático y visualización de funciones.

### Sección 43 — Lista de comprobación (análisis)

Se repasó el checklist final del laboratorio contra lo efectivamente implementado y probado:

- [x] Números reales
- [x] Suma
- [x] Resta
- [x] Multiplicación
- [x] División
- [x] Paréntesis
- [x] Variables
- [x] Potencia
- [x] Operadores unarios
- [x] Constantes `pi` y `e`
- [x] Funciones científicas
- [x] Comando `clear`
- [x] Comando `vars`
- [x] Comando `plot`
- [x] Visualización gráfica

Todos los ítems fueron implementados y verificados con evidencia en terminal (ver capturas referenciadas en cada sección anterior).

### Sección 44 — Reflexión final (análisis)

El laboratorio partió de una gramática muy pequeña, capaz solo de sumar y restar, y la fue extendiendo progresivamente hasta obtener un pequeño lenguaje matemático completo con variables, funciones y graficación. La arquitectura se mantuvo constante durante todo el proceso:

~~~
Gramática  -->  Lexer  -->  Parser  -->  Árbol  -->  Visitor
~~~

La idea central que atraviesa todo el ejercicio es que **la gramática define la sintaxis** (qué es válido escribir) y **el Visitor implementa la semántica** (qué significa lo que se escribió). Gracias a esta separación, fue posible extender el lenguaje pieza por pieza — agregar potencias, luego funciones, luego constantes, luego comandos, luego graficación, y finalmente los cinco retos opcionales — sin tener que reescribir lo ya construido en cada paso. Esta misma estrategia arquitectónica es la base de sistemas mucho más complejos: intérpretes de lenguajes de programación completos, compiladores, traductores entre formatos, analizadores estáticos de código y lenguajes de consulta. La calculadora científica desarrollada aquí es, en ese sentido, un primer ejemplo concreto y funcional de construcción de un DSL matemático usando ANTLR y el patrón Visitor.

---

## Sección 42 — Retos opcionales implementados

El laboratorio propone cinco retos de extensión sobre el núcleo del lenguaje. Los cinco fueron diseñados e implementados, en el mismo orden en que aparecen en la guía.

### Reto 1 — Nuevas funciones (`asin`, `acos`, `atan`, `floor`, `ceil`)

El más directo de los cinco: se amplió la regla léxica `function`, agregando las cinco funciones nuevas junto a las ya existentes:

~~~antlr
function
    : 'sin'
    | 'cos'
    | 'tan'
    | 'sqrt'
    | 'log'
    | 'ln'
    | 'abs'
    | 'exp'
    | 'asin'
    | 'acos'
    | 'atan'
    | 'floor'
    | 'ceil'
    ;
~~~

Y se agregaron los `case` correspondientes en `visitFunctionCall`, cada uno mapeando a su equivalente de la clase `Math` de Java:

~~~java
case "asin":  return Math.asin(value);
case "acos":  return Math.acos(value);
case "atan":  return Math.atan(value);
case "floor": return Math.floor(value);
case "ceil":  return Math.ceil(value);
~~~

No fue necesario tocar `expr` ni ningún otro archivo, porque estas funciones siguen exactamente el mismo patrón sintáctico de un solo argumento que las funciones ya existentes (`sin(x)`, `sqrt(x)`, etc.).

![Reto 1](capturas/reto1.png)
![Reto 1.2](capturas/reto1.2.png)
![Reto 1.3](capturas/reto1.3.png)

Prueba realizada:
~~~
asin(1)
acos(1)
atan(1)
floor(3.7)
ceil(3.2)
~~~
Resultados obtenidos: `asin(1) ≈ 1.5708` (π/2), `acos(1) = 0.0`, `atan(1) ≈ 0.7854` (π/4), `floor(3.7) = 3.0`, `ceil(3.2) = 4.0`.

### Reto 2 — Funciones con dos argumentos (`pow`, `max`, `min`)

Este reto requirió separar las funciones de un argumento de las de dos, porque mezclarlas en una sola regla de gramática generaría ambigüedad (el parser no sabría, solo con ver una coma, si separa dos argumentos de la misma función o si empieza otro elemento). Se creó una regla léxica independiente, `function2`, y una alternativa nueva en `expr`:

~~~antlr
expr
    : <assoc=right> expr '^' expr        # power
    | expr op=('*'|'/') expr             # mulDiv
    | expr op=('+'|'-') expr             # addSub
    | function2 '(' expr ',' expr ')'    # functionCall2
    | function '(' expr ')'              # functionCall
    | op=('+'|'-') expr                  # unary
    | constant                           # constantExpr
    | NUMBER                             # number
    | ID                                 # id
    | '(' expr ')'                       # parens
    ;

function2
    : 'pow'
    | 'max'
    | 'min'
    ;
~~~

Se implementó `visitFunctionCall2`, que evalúa ambos argumentos (`ctx.expr(0)` y `ctx.expr(1)`) y aplica el método correspondiente:

~~~java
@Override
public Double visitFunctionCall2(ScientificCalcParser.FunctionCall2Context ctx) {
    String function = ctx.function2().getText();
    double a = visit(ctx.expr(0));
    double b = visit(ctx.expr(1));

    switch (function) {
        case "pow": return Math.pow(a, b);
        case "max": return Math.max(a, b);
        case "min": return Math.min(a, b);
        default:
            throw new RuntimeException("Funcion desconocida: " + function);
    }
}
~~~

![Reto 2](capturas/reto2.png)
![Reto 2.2](capturas/reto2.2.png)
![Reto 2.3](capturas/reto2.3.png)

Prueba realizada:
~~~
pow(2,8)
max(10,25)
min(10,25)
~~~
Resultados obtenidos: `256.0`, `25.0`, `10.0`.

### Reto 3 — Rango vertical explícito en `plot` (`plot(expr,xmin,xmax,ymin,ymax)`)

Se hizo que el rango vertical fuera **opcional** en la gramática, usando un grupo opcional `(...)?` que agrupa las dos expresiones adicionales:

~~~antlr
| 'plot' '(' expr ',' expr ',' expr (',' expr ',' expr)? ')' NEWLINE   # plotExpr
~~~

Esto significa que `ctx.expr()` (la lista completa de expresiones dentro del `plot`) tiene **3 elementos** si no se especifica rango vertical, o **5** si sí se especifica. En `PlotWindow.java` se agregó un segundo constructor que recibe `ymin`/`ymax` explícitos, guardando internamente si se debe usar ese rango fijo o calcularlo automáticamente a partir de los datos (como se hacía antes):

~~~java
private boolean rangoFijo;
private double ymin;
private double ymax;

public PlotWindow(List<Double> xs, List<Double> ys, double ymin, double ymax) {
    this.xs = xs;
    this.ys = ys;
    this.rangoFijo = true;
    this.ymin = ymin;
    this.ymax = ymax;
    abrirVentana();
}
~~~

Y en `visitPlotExpr` se revisa cuántas expresiones vinieron para decidir cuál constructor usar:

~~~java
if (ctx.expr().size() == 5) {
    double ymin = visit(ctx.expr(3));
    double ymax = visit(ctx.expr(4));
    new PlotWindow(xs, ys, ymin, ymax);
} else {
    new PlotWindow(xs, ys);
}
~~~

![Reto 3](capturas/reto3.png)
![Reto 3.2](capturas/reto3.2.png)
![Reto 3.3](capturas/reto3.3.png)
![Reto 3.4](capturas/reto3.4.png)

Prueba realizada:
~~~
plot(sin(x), -6.28, 6.28)
plot(sin(x), -6.28, 6.28, -2, 2)
~~~
La primera gráfica usa el rango vertical automático (ajustado a los valores reales del seno, entre -1 y 1). La segunda fuerza el eje Y entre -2 y 2, haciendo que la curva se vea "más comprimida" verticalmente, sin ocupar todo el alto de la ventana — confirmando visualmente que el rango fijo se respeta.

### Reto 4 — Graficar varias funciones en la misma ventana (`plot(sin(x),cos(x),-6.28,6.28)`)

El diseño más delicado de los cinco: con solo comas, la gramática no puede distinguir si un elemento adicional es otra función a graficar o es parte del rango numérico. La solución adoptada fue usar `;` (punto y coma) exclusivamente para separar funciones entre sí, dejando la coma reservada para los límites numéricos:

~~~
plot(sin(x); cos(x), -6.28, 6.28)
~~~

Se usaron **etiquetas de lista** de ANTLR (`funcs+=expr`) para acumular automáticamente todas las funciones en una lista, y etiquetas simples (`xmin=`, `xmax=`, `ymin=`, `ymax=`) para los límites, evitando tener que contar manualmente cuántos elementos había (como se hizo, de forma más artesanal, en el reto 3):

~~~antlr
| 'plot' '(' funcs+=expr (';' funcs+=expr)* ',' xmin=expr ',' xmax=expr (',' ymin=expr ',' ymax=expr)? ')' NEWLINE   # plotExpr
~~~

Con estas etiquetas, el `PlotExprContext` generado expone directamente `ctx.funcs` (una `List<ExprContext>`), `ctx.xmin`, `ctx.xmax`, `ctx.ymin`, `ctx.ymax` (estos dos últimos `null` si no se especificó rango vertical).

`PlotWindow.java` se amplió para recibir listas de listas (una lista de curvas, cada una con sus propios puntos `x`/`y`), asignando un color distinto a cada curva desde un arreglo fijo:

~~~java
private static final Color[] COLORES = {
    Color.BLUE, Color.RED, Color.GREEN, Color.ORANGE, Color.MAGENTA
};
~~~

y calculando los límites de la ventana (`xmin`, `xmax`, `ymin`, `ymax`) considerando **todas** las curvas juntas, para que quepan simultáneamente. El método `visitPlotExpr` final recorre `ctx.funcs` con un simple `for`, repitiendo para cada función el mismo bucle de muestreo de 800 puntos que ya existía, pero acumulando los resultados en listas de listas:

~~~java
for (var funcExpr : ctx.funcs) {
    List<Double> xs = new ArrayList<>();
    List<Double> ys = new ArrayList<>();

    for (int i = 0; i < samples; i++) {
        double x = xmin + i * (xmax - xmin) / (samples - 1);
        memory.put("x", x);
        double y = visit(funcExpr);

        if (Double.isFinite(y)) {
            xs.add(x);
            ys.add(y);
        }
    }

    seriesXs.add(xs);
    seriesYs.add(ys);
}
~~~

![Reto 4](capturas/reto4.png)
![Reto 4.2](capturas/reto4.2.png)
![Reto 4.3](capturas/reto4.3.png)
![Reto 4.4](capturas/reto4.4.png)
![Reto 4.5](capturas/reto4.5.png)

Prueba realizada:
~~~
plot(sin(x), -6.28, 6.28)
plot(sin(x); cos(x), -6.28, 6.28)
plot(sin(x); cos(x), -6.28, 6.28, -2, 2)
~~~
La primera confirma que la sintaxis original (una sola función) sigue funcionando sin cambios. La segunda muestra seno y coseno superpuestos en la misma ventana, cada uno con su color. La tercera combina esto con el reto 3, forzando además el rango vertical entre -2 y 2.

### Reto 5 — Definir funciones propias del usuario (`f(x) = x^2 + 2*x + 1`)

El reto más ambicioso: requiere que el lenguaje pueda **recordar una expresión sin evaluarla todavía** (el cuerpo de la función) y evaluarla más tarde, cada vez con un valor distinto para su parámetro — el mismo mecanismo ya usado para graficar, pero generalizado a cualquier función definida por el usuario, no solo a `x`.

Se agregaron dos reglas nuevas a la gramática: una instrucción de definición (`funcDef`) y una llamada a función de usuario dentro de una expresión (`userFunctionCall`):

~~~antlr
stat
    : expr NEWLINE                    # printExpr
    | ID '(' ID ')' '=' expr NEWLINE  # funcDef
    | ID '=' expr NEWLINE             # assign
    ...
    ;

expr
    : ...
    | ID '(' expr ')'                 # userFunctionCall
    ...
    ;
~~~

En `funcDef`, hay dos tokens `ID` en la misma alternativa: `ctx.ID(0)` es el nombre de la función (`f`), `ctx.ID(1)` es el nombre de su parámetro (`x`). ANTLR distingue automáticamente esta alternativa de una asignación normal (`ID '=' expr`) y de una llamada (`ID '(' expr ')'`), simplemente por la forma de los tokens que siguen al primer identificador — no hay ambigüedad real, aunque se parezcan a simple vista.

Se agregaron dos mapas nuevos al Visitor: uno que recuerda el nombre del parámetro de cada función definida, y otro que recuerda su cuerpo **sin evaluar** (el `ExprContext` tal cual, para revisitarlo después):

~~~java
Map<String, String> funcParams = new HashMap<>();
Map<String, ScientificCalcParser.ExprContext> funcBodies = new HashMap<>();

@Override
public Double visitFuncDef(ScientificCalcParser.FuncDefContext ctx) {
    String nombreFuncion = ctx.ID(0).getText();
    String nombreParametro = ctx.ID(1).getText();

    funcParams.put(nombreFuncion, nombreParametro);
    funcBodies.put(nombreFuncion, ctx.expr());

    System.out.println("Funcion definida: " + nombreFuncion + "(" + nombreParametro + ")");
    return 0.0;
}
~~~

La parte más delicada es `visitUserFunctionCall`: cuando se llama `f(5)`, hay que evaluar el cuerpo guardado de `f` (por ejemplo `x^2 + 2*x + 1`), pero ese cuerpo usa el nombre `x`, que podría chocar con una variable `x` que el usuario ya tuviera definida por otro lado (por ejemplo, si se estaba graficando algo previamente). Por eso se guarda y restaura el valor previo de esa variable:

~~~java
@Override
public Double visitUserFunctionCall(ScientificCalcParser.UserFunctionCallContext ctx) {
    String nombreFuncion = ctx.ID().getText();

    String nombreParametro = funcParams.get(nombreFuncion);
    ScientificCalcParser.ExprContext cuerpo = funcBodies.get(nombreFuncion);

    double valorArgumento = visit(ctx.expr());

    Double valorPrevio = memory.get(nombreParametro);
    memory.put(nombreParametro, valorArgumento);

    double resultado = visit(cuerpo);

    if (valorPrevio != null) {
        memory.put(nombreParametro, valorPrevio);
    } else {
        memory.remove(nombreParametro);
    }

    return resultado;
}
~~~

Este "guardar y restaurar" es lo que permite, incluso, combinar llamadas a funciones de usuario con graficación o con otras variables sin que se pisen los valores entre sí.

![Reto 5](capturas/reto5.png)
![Reto 5.2](capturas/reto5.2.png)
![Reto 5.3](capturas/reto5.3.png)
![Reto 5.4](capturas/reto5.4.png)

Prueba realizada:
~~~
f(x) = x^2 + 2*x + 1
f(5)
f(0)
f(-1)
plot(f(x), -10, 10)
~~~
Resultados obtenidos: `f(5) = 36.0`, `f(0) = 1.0`, `f(-1) = 0.0` (coincidiendo con el cálculo manual, ya que `f(x) = (x+1)²`). La gráfica muestra correctamente una parábola con su mínimo (valor 0) exactamente en `x = -1`, confirmando que la función definida por el usuario se integra sin fricción con el comando `plot`, tal como cualquier función incorporada del lenguaje.

