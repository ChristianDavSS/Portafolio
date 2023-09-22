# Ejercicio 4
Obtener la edad promedio de n personas preguntandoles su año de nacimiento y asumiendo que el año actual es 2023

ANALISIS:

1.- Como el enunciado nos dice que son n personas, debemos comenzar preguntando la cantidad de personas y, al ser un promedio, verificar con una condicional que sea mayor o igual a dos. Si no es así, lo regresará a que ingrese el numero nuevamente.

2.- Una vez pasada la primera condicional, vamos a preguntar el año de nacimiento de la persona y vamos a verificar que sea menor o igual a 2023, que es el año actual. De no ser así, lo regresará a que la ingrese nuevamente.

3.- Va a guardar en una variable llamada “edad” la resta de 2023 menos el año de nacimiento, después va a contar cuantas personas van con un contador (c) y a acumular la edad (s).

4.- Seguido de esto, crearemos un ciclo con ayuda de una condicional. Si el contador es menor al número de personas entonces el ciclo se repite y preguntará el año de nacimiento a la siguiente persona. 

5.- Una vez la condicional de “no”; vamos a sacar el promedio dividiendo el acumulador entre el contador.

6.- Imprimiremos en pantalla el resultado.

# DIAGRAMA DE FLUJO
![edad_n_personas EJ 4](https://github.com/ChristianDavSS/Portafolio/assets/145722756/c8ded894-a6b1-4591-a854-fe17024fee48)

# PRUEBA DE ESCRITORIO
![Prueba de escritorio 4](https://github.com/ChristianDavSS/Portafolio/assets/145722756/8d6c341f-42f3-4a90-a06f-d23456f507b9)
