# Tarea Conjuntos

Cálculo de PRIMEROS, SIGUIENTES y PREDICCIÓN para las dos gramáticas de la tarea, con tabla LL(1).

## Archivos

- `conjuntos.py` - funciones para sacar anulables, primeros, siguientes, predicción y la tabla.
- `main.py` - tiene las 2 gramáticas y muestra los resultados en consola.

## Cómo correrlo

```bash
cd "Tarea Conjuntos"
python3 main.py
```

Con `python3 main.py 1` se corre solo el ejercicio 1 y con `python3 main.py 2` solo el 2.

## Ejercicio 1

![Ejercicio 1](<Imagenes Ejercicios/Ejercicio_1.png>)

![Ejecucion](<Programa_Ejecutado/Ejercicio1/ejecucion.png>)

![Primeros 1](<Programa_Ejecutado/Ejercicio1/primeros1.png>)

![Siguientes 1](<Programa_Ejecutado/Ejercicio1/siguientes1.png>)

![Prediccion 1](<Programa_Ejecutado/Ejercicio1/Prediccion1.png>)

No es LL(1). Hay choques en S, en A, en M[B, seis] y en M[D, seis. Además tiene recursión por la izquierda en S -> S dos y A -> A tres.

## Ejercicio 2

![Ejercicio 2](<Imagenes Ejercicios/Ejercicio_2.png>)

![Ejecucion 2](<Programa_Ejecutado/Ejercicio2/ejecucion2.png>)

![Primeros 2](<Programa_Ejecutado/Ejercicio2/primeros2.png>)

![Siguientes 2](<Programa_Ejecutado/Ejercicio2/siguientes2.png>)

![Prediccion 2](<Programa_Ejecutado/Ejercicio2/prediccion2.png>)

Tampoco es LL(1). Hay choques en M[B, tres], M[B, cuatro], M[B, cinco] y en M[D, seis].
