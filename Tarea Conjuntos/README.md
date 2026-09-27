# Tarea Conjuntos

## Integrantes

- Camilo Bernal
- Diego Moreno
- Yeisson Rincón

Cálculo de PRIMEROS, SIGUIENTES y PREDICCIÓN para las dos gramáticas de la tarea, junto con la tabla LL(1).

## Archivos

- `conjuntos.py` - funciones para calcular anulables, primeros, siguientes, predicción y la tabla LL(1).
- `main.py` - define las 2 gramáticas y presenta los resultados en consola.

## Ejecución

```bash
cd "Tarea Conjuntos"
python3 main.py
```

El comando `python3 main.py 1` ejecuta únicamente el ejercicio 1, y `python3 main.py 2` ejecuta únicamente el ejercicio 2.

## Ejercicio 1

![Ejercicio 1](<Imagenes Ejercicios/Ejercicio_1.png>)

### Resultados por programa (consola)

![Ejecucion](<Programa_Ejecutado/Ejercicio1/ejecucion.png>)

![Primeros 1](<Programa_Ejecutado/Ejercicio1/primeros1.png>)

![Siguientes 1](<Programa_Ejecutado/Ejercicio1/siguientes1.png>)

![Prediccion 1](<Programa_Ejecutado/Ejercicio1/Prediccion1.png>)

### Solución a mano

![Ejercicio 1 a mano](<Imagenes Ejercicios a Mano/Ejercicio 1.jpeg>)

Esta gramática no es LL(1). Presenta choques en S, en A, en M[B, seis] y en M[D, seis]. Además tiene recursión por la izquierda en las producciones S -> S dos y A -> A tres.

## Ejercicio 2

![Ejercicio 2](<Imagenes Ejercicios/Ejercicio_2.png>)

### Resultados por programa (consola)

![Ejecucion 2](<Programa_Ejecutado/Ejercicio2/ejecucion2.png>)

![Primeros 2](<Programa_Ejecutado/Ejercicio2/primeros2.png>)

![Siguientes 2](<Programa_Ejecutado/Ejercicio2/siguientes2.png>)

![Prediccion 2](<Programa_Ejecutado/Ejercicio2/prediccion2.png>)

### Solución a mano

![Ejercicio 2 a mano](<Imagenes Ejercicios a Mano/Ejercicio 2.jpeg>)

![Ejercicio 2 a mano 2](<Imagenes Ejercicios a Mano/Ejercicio2_1.jpeg>)

Esta gramática tampoco es LL(1). Presenta choques en M[B, tres], M[B, cuatro], M[B, cinco] y en M[D, seis].
