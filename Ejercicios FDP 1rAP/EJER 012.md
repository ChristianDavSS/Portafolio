# Ejercicio 12
Una empresa desea calcular el sueldo total de una persona bajo los siguientes rubros: percepciones, sueldo base, 5% de canasta basica, 3% de prima de antiguedad y deducciones si el salario base excede los 10,000 pesos el ISR es del 30% y si es menos 20%. Indique cuanto es el total de la nomina a pagar y cuantos son los impuestos que el patron debe de pagar al SAT.

ANALISIS:

Para este diagrama, vamos a hacer que calcule las percepciones con base al sueldo de la cantidad de empleados que se ingresen, además de los impuestos. Al final, vamos a imprimir los impuestos de ISR que tiene que pagar el jefe y la nómina que tiene que pagar a los empleados.

1.- Primero, al ser n empleados, tenemos que preguntar la cantidad y verificar que sean mas que 0. De otro modo, pedira que ingrese otro numero.

2.- Despues se preguntará el sueldo base y, asegurandonos que sea mayor que 0, calcularemos todas las percepciones y, ya calculadas, la guardaremos en un acumulador.

3.- Despues, con una condicional, vamos a verificar si el sueldo base es menor que 10,000 y, de ser asi, vamos a restarle al sueldo total (ya con percepciones) el 20% del ISR y a acumularlo en i1. En caso de que el sueldo base sea mayor a 10,000 entonces vamos a restarle el 30% de ISR y a acumularlo en i2.

4.- Ya que hayamos sacado tanto las percepciones como el ISR, entonces vamos a contar uno a uno con c los empleados a los que ya se les haya calculado.

5.- Con un ciclo, esta que si el contador es menor que la cantidad de empleados entonces se repetiran los pasos anteriores hasta que el contador no sea menor que estos.

6.- Una vez el contador no sea menor que la cantidad de empleados, entonces se imprimirá en pantalla la nomina a pagar (sp) y los impuestos (i1 y i2) de los trabajadores.

# DIAGRAMA DE FLUJO
![empresaimpuestos EJ 12](https://github.com/ChristianDavSS/Portafolio/assets/145722756/db1d39d2-7259-424e-afe9-fc7bf83f47eb)

# PRUEBA DE ESCRITORIO
![Prueba de escritorio 12](https://github.com/ChristianDavSS/Portafolio/assets/145722756/9e6b541f-c90c-4ea9-935f-dd1c2bc1b4cd)
