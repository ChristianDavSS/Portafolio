# Ejercicio 8: Se te proporcionan dos matrices cuadradas, A y B, de tamaño NxN. Su tarea es desarrollar un
# algoritmo que realice la suma de estas dos matrices, resultando en una tercera matriz cuadrada, C.
#Christian David Sánchez Sánchez 1°B
import random

filas = 100
columnas = 100

while True:
    n:int = int(input("Ingresa n para las matrices: "))
    if n <= 0 or n > 100:
        print("Ingresa un número valido")
    else:
        break

a = [[(random.randint(1,50))for _ in range(n)]for _ in range(n)]
b = [[(random.randint(1,50))for _ in range(n)]for _ in range(n)]
c = [[0 for _ in range(n)]for _ in range(n)]

#Imprimir matriz 1:
print("Matriz 1:")
for i in range(n):
    for j in range(n):
        print(f"{a[i][j]}", end= " ")
    print()
print()

#Imprimir matriz 2:
print("Matriz 2:")
for i in range(n):
    for j in range(n):
        print(f"{b[i][j]}", end= " ")
    print()
print()

#Suma de matrices
print("La suma de las matrices es:")
for i in range(n):
    for j in range(n):
        c[i][j] = a[i][j] + b[i][j]
        print(f"{c[i][j]}", end = " ")
    print()