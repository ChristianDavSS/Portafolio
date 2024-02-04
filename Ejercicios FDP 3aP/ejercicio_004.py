# Ejercicio 4: Dado un array de números enteros, encuentre el valor máximo y mínimo en el array.
# Christian David Sánchez Sánchez 1°B
import random
arreglo = [(random.randint(1,50))for _ in range(7)]
maximo = arreglo[0]
minimo = arreglo[0]


for i in range(len(arreglo)):
    if arreglo[i] > maximo:
        maximo = arreglo[i]
    elif arreglo[i] < minimo:
        minimo = arreglo[i]

print(arreglo)
print(f"El valor maximo es: {maximo}")
print(f"El valor minimo es: {minimo}")