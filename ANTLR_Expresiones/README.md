# Tareas ANTLR — Análisis Sintáctico (Linux)

Proyectos Python + ANTLR 4.13.2 de las diapositivas 11, 12/13 y 15.
Todo lo de aquí es para Linux (bash).

## Estructura

```
Tareas/
  README.md           <- este archivo
  requirements.txt    <- dependencia para pip
  Tarea #1/           <- Diapo 11: E -> E+T|T, T -> T*F|F, F -> id|num|(E)
    main.py, casos.txt, Expr11.g4, Expr11*.py, generar.sh
  Tarea #2/           <- Diapos 12/13/14: Parse Tree vs AST para 3+4*5
    main.py, casos.txt, Expr12.g4, Expr12*.py, generar.sh
  Tarea #3/           <- Diapo 15: E -> E+E|E*E|num (ambigua), 2+3*4 = 20 vs 14
    main.py, casos.txt, ExprAmb.g4, ExprAmbInv.g4, ExprAmb*.py, generar.sh
```

## Requisitos

- Linux con `python3` (>= 3.10), `pip3` y `java` (Java solo para regenerar el parser; para ejecutar no hace falta).
- Solo 1 dependencia Python: `antlr4-python3-runtime==4.13.2` (ver `requirements.txt`).

Comprobar versiones:

```bash
python3 --version
pip3 --version
java -version   # solo necesario para ./generar.sh
```

## 1. Crear entorno virtual (recomendado)

Desde esta carpeta:

```bash
cd ~/Tareas
python3 -m venv .venv
source .venv/bin/activate
```

Verás `(.venv)` al inicio del prompt. Para salir: `deactivate`.

## 2. Instalar dependencias

Con el venv activado:

```bash
pip install -r requirements.txt
```

O instalación directa sin `requirements.txt`:

```bash
pip install antlr4-python3-runtime==4.13.2
```

Verificar:

```bash
pip show antlr4-python3-runtime
python3 -c "import antlr4; print(antlr4.__version__)"
```

## 3. Cómo iniciar cada programa

Todos funcionan igual: leen un `.txt` (una expresión por línea), dicen `ACEPTADA / RECHAZADA` y evalúan.

### Tarea #1 — Gramática tal cual diapo 11

```bash
cd ~/Tareas/"Tarea #1"
python3 main.py casos.txt
python3 main.py "2 + 3 * 4"
python3 main.py "a + b * c | a=2 b=3 c=4"
python3 main.py
```

- `main.py:26-32` silencia errores de ANTLR y los cuenta para imprimir `Estado`.
- `main.py:35-58` `EvalVisitor` evalúa `+` y `*` con asociatividad izquierda.
- Formato `casos.txt`: `expresion [| var=valor ...]`, `#` es comentario, línea vacía se ignora.
- Esperado: `2+3*4=14` ACEPTADA, `2+3-4` RECHAZADA (no hay `-` en la gramática tal cual), `2+*3` RECHAZADA.

### Tarea #2 — Parse Tree vs AST

```bash
cd ~/Tareas/"Tarea #2"
python3 main.py casos.txt
python3 main.py "3 + 4 * 5"
python3 main.py "a + b * c | a=2 b=3 c=4"
```

- Por cada caso muestra: `[1]` Parse Tree completo con `E,T,F`, `[2]` AST en 3 formas (ASCII / tupla / JSON) + evaluación, `[3]` comparativa Parse vs AST, `[4]` correcto `+(3,*(4,5))=23` vs incorrecto `*(+(3,4),5)=35`.
- Esperado: `3+4*5=23` ACEPTADA, `3+*5` RECHAZADA.

### Tarea #3 — Gramática ambigua

```bash
cd ~/Tareas/"Tarea #3"
python3 main.py casos.txt
python3 main.py "2 + 3 * 4"
```

- Parsea 2 veces: `ExprAmb.g4` (`+` primero → `(2+3)*4=20`) y `ExprAmbInv.g4` (`*` primero → `2+(3*4)=14`). Mismo input, dos árboles = AMBIGUA comprobada.
- Esperado: `2+3*4` ACEPTADA con `20 vs 14`, `2+*3` y `a+b` RECHAZADAS (solo existe `num`, no `id` ni `*` huérfano).

Sin argumentos, cada `main.py` usa su `casos.txt` por defecto.

## Regenerar el parser (solo si editas un .g4)

```bash
cd ~/Tareas/"Tarea #1"
chmod +x generar.sh
./generar.sh
```

El script busca el jar en `$ANTLR_JAR` o en `/tmp/antlr-4.13.2-complete.jar`. Para descargarlo:

```bash
curl -L -o /tmp/antlr-4.13.2-complete.jar https://www.antlr.org/download/antlr-4.13.2-complete.jar
```

Genera `Expr*Lexer.py`, `Expr*Parser.py`, `Expr*Visitor.py`.

## Permisos

Si `main.py` o `generar.sh` no ejecutan:

```bash
chmod +x main.py generar.sh
./main.py casos.txt
```

## Problemas comunes

- `ModuleNotFoundError: antlr4` → no instalaste la dependencia o no activaste el venv. Repite los pasos 1 y 2.
- `No se encontro ...antlr-*.jar` / `java: command not found` → solo afecta a `./generar.sh`, no a `main.py`. Instala Java (`sudo apt install default-jre`) y descarga el jar como arriba.
- `identificador sin valor` → es ERROR semántico, no sintáctico: el Estado sigue siendo ACEPTADA. Pasa valores con `| a=2 b=3 c=4` en el `.txt`.
- Rutas con espacios (`Tarea #1`) → usa comillas en bash como en los ejemplos.
