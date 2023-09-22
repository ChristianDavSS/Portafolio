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
![](file:///C:/Users/Sanch/OneDrive/Desktop/ICI%201°B/PORTAFOLIO%20FUNDAMENTOS/en%20fotito/edad_n_personas%20EJ%204.png)

# PRUEBA DE ESCRITORIO
![](file:///C:/Users/Sanch/OneDrive/Desktop/ICI%201°B/PORTAFOLIO%20FUNDAMENTOS/PRUEBAS%20PNG/Prueba%20de%20escritorio%204.png)