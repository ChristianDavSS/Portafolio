# Ejercicio 16
La tienda "Brankos" debe vender productos a n alumnos, ofrecen: tacos, tortas, hotdogs y pizzas. Imprime los productos vendidos en total.

ANALISIS:

Este diagrama de flujo calcula la cantidad de productos que Brankos vendió a cierta cantidad de alumnos.

1.- Primero, al ser n alumnos, debemos preguntar la cantidad y verificar que sean mas de 0.

2.- Vamos a desplegar el menú que Branks tiene para ver que quiere ordenar el usuario, ya que ordene vamos a verificar que el numero sea mayor o igual a uno y menor o igual a 4, ya que son 4 productos.

3.- Vamos a desplegar un switch o match, en el que el valor que el usuario haya ingresado sea el camino que se tome para que se cuente el pedido. Cada camino tiene un contador integrado, ya que queremos llegar a la cantidad de ventas totales.

4.- Una vez pasado el switch, vamos a encontrar un contador el cual cuenta cuantos alumnos ingresaron su orden.

5.- Con un ciclo, vamos a definir que si el numero de alumnos es mayor al contador, se repota el ciclo nuevamente hasta que esta condicion no se cumpla.

6.- Cuando no se cumpla, vamos a relalizar la suma de todos los contadores que estaban en los 4 caminos de pedidos, y se nos va a imprimir en pantalla cuantos productos fueron vendidos.

# DIAGRAMA DE FLUJO
![Brankos_ventas EJ 16](https://github.com/ChristianDavSS/Portafolio/assets/145722756/181597bf-5cb6-4ad6-929f-2b4fb9f4d913)

# PRUEBA DE ESCRITORIO
![Prueba de escritorio 16](https://github.com/ChristianDavSS/Portafolio/assets/145722756/716ad490-09a2-489c-ac15-5d96fb0c8c2e)
