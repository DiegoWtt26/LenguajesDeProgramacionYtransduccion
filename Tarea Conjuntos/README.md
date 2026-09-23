# Tarea Conjuntos

## Integrantes

- Camilo Bernal
- Diego Moreno
- Yeisson Rincón

Cálculo de PRIMEROS, SIGUIENTES y PREDICCIÓN para las dos gramáticas, con tabla LL(1).

## Archivos

- `conjuntos.py` - funciones de anulables, primeros, siguientes, predicción y tabla.
- `main.py` - definición de las 2 gramáticas y salida en consola.

## Ejecución

```bash
cd "Tarea Conjuntos"
python3 main.py
```

`python3 main.py 1` para el ejercicio 1, `python3 main.py 2` para el 2.

## Ejercicio 1

![Ejercicio 1](<Imagenes Ejercicios/Ejercicio_1.png>)

![Ejecucion](<Programa_Ejecutado/Ejercicio1/ejecucion.png>)

![Primeros 1](<Programa_Ejecutado/Ejercicio1/primeros1.png>)

![Siguientes 1](<Programa_Ejecutado/Ejercicio1/siguientes1.png>)

![Prediccion 1](<Programa_Ejecutado/Ejercicio1/Prediccion1.png>)

Resultado: no LL(1). Choques en S, en A, en M[B, seis] y en M[D, seis]. Recursión izquierda en S -> S dos y A -> A tres.

## Ejercicio 2

![Ejercicio 2](<Imagenes Ejercicios/Ejercicio_2.png>)

![Ejecucion 2](<Programa_Ejecutado/Ejercicio2/ejecucion2.png>)

![Primeros 2](<Programa_Ejecutado/Ejercicio2/primeros2.png>)

![Siguientes 2](<Programa_Ejecutado/Ejercicio2/siguientes2.png>)

![Prediccion 2](<Programa_Ejecutado/Ejercicio2/prediccion2.png>)

Resultado: no LL(1). Choques en M[B, tres], M[B, cuatro], M[B, cinco] y en M[D, seis].
