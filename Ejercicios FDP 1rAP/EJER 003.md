# Ejercicio 3
Obtenga el promedio de n números positivos leídos del teclado

ANALISIS:

Vamos a crear un dfd que saque el promedio de los números que el usuario ingrese.

1.- Tenemos que preguntar la cantidad de números que vamos a promediar y almacenarlos para utilizarlos más adelante y, con una condicional, verificar si esta cantidad es igual o mayor a 2 ya que estamos hablando de promedio.

2.- Pedimos un numero y lo verificamos, con una condicional, que sea mayor o igual a 0, de ser así lo contamos y acumulamos, de lo contrario lo regresamos a ingresar el numero nuevamente.

3.- Una vez pasado el paso anterior, con una condicional creamos un ciclo. Si es contador es menor que la cantidad de numeros deseada, va a regresar a pedirte un numero y esto se repetirá hasta que esta condición no se cumpla.

4.- Ya que no se cumpla esta condición y el bucle finalice, va a sacar el promedio dividiendo el acumulador entre el contador (p = s / c).

5.- Se imprimirá en pantalla el promedio.

# DIAGRAMA DE FLUJO
![promedio_n_numeros EJ 3](https://github.com/ChristianDavSS/Portafolio/assets/145722756/5ffca088-30aa-41ae-aa24-c9ea4de67c87)

# PRUEBA DE ESCRITORIO
![Prueba de escritorio 3](https://github.com/ChristianDavSS/Portafolio/assets/145722756/bfb6b067-c108-49a4-a0c6-f0e5d1254015)
