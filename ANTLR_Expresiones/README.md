# Tareas ANTLR — Análisis sintáctico (Linux)

## Integrantes

- Camilo Bernal
- Diego Moreno
- Yeisson Rincón

Programas en Python con ANTLR 4.13.2 correspondientes a las diapositivas 11, 12/13 y 15. Todo el trabajo está probado en Linux con bash.

## Estructura

```
Tareas/
  README.md           <- este archivo
  requirements.txt
  Tarea #1/           <- Diapo 11: E -> E+T|T, T -> T*F|F, F -> id|num|(E)
  Tarea #2/           <- Diapos 12/13/14: Parse Tree vs AST con 3+4*5
  Tarea #3/           <- Diapo 15: E -> E+E|E*E|num (ambigua), 2+3*4 = 20 vs 14
```

## Requisitos

- Linux con `python3` (versión 3.10 o superior), `pip3` y `java` (Java se necesita únicamente para regenerar el parser; para ejecutar los programas no hace falta).
- Una sola dependencia de Python: `antlr4-python3-runtime==4.13.2`.

```bash
python3 --version
pip3 --version
java -version   # solo necesario para ./generar.sh
```

## 1. Entorno virtual (recomendado)

Desde esta carpeta se crea y se activa el entorno:

```bash
cd ~/Tareas
python3 -m venv .venv
source .venv/bin/activate
```

Al activarlo aparece `(.venv)` al inicio del prompt. Para salir del entorno se usa `deactivate`.

## 2. Instalación de dependencias

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

La instalación también se puede hacer de forma directa, sin el archivo de requisitos:

```bash
pip install antlr4-python3-runtime==4.13.2
```

Para verificar que quedó bien instalado:

```bash
pip show antlr4-python3-runtime
python3 -c "import antlr4; print(antlr4.__version__)"
```

## 3. Ejecución de cada programa

Los tres programas funcionan de la misma manera: leen un archivo de texto (una expresión por línea), indican `ACEPTADA` o `RECHAZADA` para cada una y muestran su evaluación.

### Tarea #1 — diapo 11

```bash
cd ~/Tareas/"Tarea #1"
python3 main.py casos.txt
python3 main.py "2 + 3 * 4"
python3 main.py "a + b * c | a=2 b=3 c=4"
python3 main.py
```

El formato de `casos.txt` es `expresion [| var=valor]` y el símbolo `#` marca un comentario. El resultado esperado es `2+3*4=14` como ACEPTADA, `2+3-4` como RECHAZADA (la gramática no incluye el operador `-`) y `2+*3` como RECHAZADA.

### Tarea #2 — Parse Tree vs AST

```bash
cd ~/Tareas/"Tarea #2"
python3 main.py casos.txt
python3 main.py "3 + 4 * 5"
python3 main.py "a + b * c | a=2 b=3 c=4"
```

Por cada caso el programa muestra el Parse Tree completo, el AST en tres formas (ASCII, tupla y JSON) con su valor evaluado, la comparación entre Parse Tree y AST, y el contraste entre el árbol correcto `+(3,*(4,5))=23` y el incorrecto `*(+(3,4),5)=35`.

### Tarea #3 — gramática ambigua

```bash
cd ~/Tareas/"Tarea #3"
python3 main.py casos.txt
python3 main.py "2 + 3 * 4"
```

El programa analiza dos veces: con `ExprAmb.g4` (el `+` primero, lo que agrupa `(2+3)*4=20`) y con `ExprAmbInv.g4` (el `*` primero, lo que agrupa `2+(3*4)=14`). Que el mismo texto produzca dos árboles distintos demuestra la ambigüedad.

Si no se indica ningún argumento, cada programa utiliza su archivo `casos.txt` por defecto.

## Regeneración del parser (solo si cambia algún .g4)

```bash
cd ~/Tareas/"Tarea #1"
chmod +x generar.sh
./generar.sh
```

El script busca el archivo jar en la variable `$ANTLR_JAR` o en la ruta `/tmp/antlr-4.13.2-complete.jar`. Si no existe, se descarga con:

```bash
curl -L -o /tmp/antlr-4.13.2-complete.jar https://www.antlr.org/download/antlr-4.13.2-complete.jar
```

El script genera los archivos `Expr*Lexer.py`, `Expr*Parser.py` y `Expr*Visitor.py`.

## Permisos

Si `main.py` o `generar.sh` no se dejan ejecutar, se les da permiso con:

```bash
chmod +x main.py generar.sh
./main.py casos.txt
```

## Problemas comunes

- `ModuleNotFoundError: antlr4` → la dependencia no está instalada o el entorno virtual no está activado. Se soluciona repitiendo los pasos 1 y 2.
- `No se encontro ...antlr-*.jar` / `java: command not found` → este error solo afecta a `./generar.sh`, el archivo `main.py` sigue funcionando. Se soluciona instalando Java (`sudo apt install default-jre`) y descargando el jar como se indica arriba.
- `identificador sin valor` → es un error semántico, no sintáctico, por lo que el estado sigue siendo ACEPTADA. Para corregirlo se pasan los valores con la sintaxis `| a=2 b=3 c=4`.
- Las carpetas tienen espacios en el nombre (`Tarea #1`), por lo que en bash las rutas se escriben entre comillas, como en los ejemplos.
