# Ejercicio 9
Capture n numeros enteros positivos, obtenga la suma del cuadrado de los pares y el cubo de los impares.

ANALISIS:

Este dfd nos va a permitir ingresar la cantidad de numeros que queramos, y que el numero que ingresemos se eleve al cuadrado o al cubo dependiendo si es par o no.

1.- Primero se pide que se especifiquen la cantidad de numeros y se verifica que el numero sea mayor a 0., de otro modo se le pedira que lo ingrese nuevamente.

2.- Se pide que ingrese el numero a evaluar y se verifica que este sea mayor o igual a 0, de otro modo le pedira que lo ingrese nuevamente.

3.- Despues, se verá si el numero ingresado es par o es impar. En caso de ser par, se acumulará con el acumulador de pares (SP) elevandose al cuadrado, pero si es impar entonces se acumulará en el acumulador de impares (SI) elevandose al cubo.

4.- Una vez pasado esto, se va a contar en el contador cuantos numeros han sido ingresados.

5.- Con ayuda de un ciclo, se verá si la cantidad de numeros es mayor a el contador, de ser asi entonces se repite el ciclo solicitando otro numero y repitiendo lo anterior.

6.- Una vez la condicion no se cumpla, se imprimirá en pantalla el acumulador de los pares y el acumulador de los impares.

# DIAGRAMA DE FLUJO
![sumacuadradosycubos EJ 9](https://github.com/ChristianDavSS/Portafolio/assets/145722756/b9f452ff-d345-4d39-b893-2b321438c813)

# PRUEBA DE ESCRITORIO
![Prueba de escritorio 9](https://github.com/ChristianDavSS/Portafolio/assets/145722756/a81718f3-b075-45b2-9e54-a6d46e2f3af1)
