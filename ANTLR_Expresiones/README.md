# Tareas ANTLR — Análisis sintáctico (Linux)

## Integrantes

- Camilo Bernal
- Diego Moreno
- Yeisson Rincón

Programas Python + ANTLR 4.13.2 de las diapos 11, 12/13 y 15. Entorno Linux (bash).

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

- Linux con `python3` (>= 3.10), `pip3` y `java` (Java solo para regenerar; ejecución sin Java).
- Dependencia única: `antlr4-python3-runtime==4.13.2`.

```bash
python3 --version
pip3 --version
java -version   # solo para ./generar.sh
```

## 1. Entorno virtual (recomendado)

Desde esta carpeta:

```bash
cd ~/Tareas
python3 -m venv .venv
source .venv/bin/activate
```

Indicador `(.venv)` al inicio del prompt. Salida con `deactivate`.

## 2. Instalación

```bash
pip install -r requirements.txt
```

Instalación directa:

```bash
pip install antlr4-python3-runtime==4.13.2
```

Verificación:

```bash
pip show antlr4-python3-runtime
python3 -c "import antlr4; print(antlr4.__version__)"
```

## 3. Ejecución de cada programa

Lectura de un txt (una expresión por línea), estado `ACEPTADA / RECHAZADA` y evaluación.

### Tarea #1 — diapo 11

```bash
cd ~/Tareas/"Tarea #1"
python3 main.py casos.txt
python3 main.py "2 + 3 * 4"
python3 main.py "a + b * c | a=2 b=3 c=4"
python3 main.py
```

Formato `casos.txt`: `expresion [| var=valor]`, `#` comentario. Resultado: `2+3*4=14` ACEPTADA, `2+3-4` RECHAZADA (sin `-` en la gramática), `2+*3` RECHAZADA.

### Tarea #2 — Parse Tree vs AST

```bash
cd ~/Tareas/"Tarea #2"
python3 main.py casos.txt
python3 main.py "3 + 4 * 5"
python3 main.py "a + b * c | a=2 b=3 c=4"
```

Salida por caso: Parse Tree completo, AST en 3 formas (ASCII / tupla / JSON) + valor, comparativa Parse vs AST, y `+(3,*(4,5))=23` frente a `*(+(3,4),5)=35`.

### Tarea #3 — ambigua

```bash
cd ~/Tareas/"Tarea #3"
python3 main.py casos.txt
python3 main.py "2 + 3 * 4"
```

Doble parseo: `ExprAmb.g4` (`+` primero → `(2+3)*4=20`) y `ExprAmbInv.g4` (`*` primero → `2+(3*4)=14`). Mismo input, dos árboles.

Sin argumentos, uso del `casos.txt` correspondiente.

## Regenerar el parser (solo con cambios en .g4)

```bash
cd ~/Tareas/"Tarea #1"
chmod +x generar.sh
./generar.sh
```

Búsqueda del jar en `$ANTLR_JAR` o `/tmp/antlr-4.13.2-complete.jar`:

```bash
curl -L -o /tmp/antlr-4.13.2-complete.jar https://www.antlr.org/download/antlr-4.13.2-complete.jar
```

Salida: `Expr*Lexer.py`, `Expr*Parser.py`, `Expr*Visitor.py`.

## Permisos

```bash
chmod +x main.py generar.sh
./main.py casos.txt
```

## Problemas comunes

- `ModuleNotFoundError: antlr4` → dependencia sin instalar o venv sin activar. Repetir pasos 1 y 2.
- `No se encontro ...antlr-*.jar` / `java: command not found` → solo afecta a `./generar.sh`. Instalación con `sudo apt install default-jre` + descarga del jar.
- `identificador sin valor` → error semántico, no sintáctico. Estado ACEPTADA. Paso de valores con `| a=2 b=3 c=4`.
- Rutas con espacios (`Tarea #1`) → uso de comillas en bash.
