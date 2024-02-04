# Ejercicio 6: Desarrolla un algoritmo que calcule la suma de todos los elementos en una matriz dada de tamaño nxm.
# Christian David Sánchez Sánchez 1°B
import random
renglones = 100
columnas = 100
s = 0
m = [[(random.randint(1,50)) for _ in range(columnas)]for _ in range(renglones)]

# Preguntar n y m
while True:
    r:int = int(input("Ingresa el valor de n (renglones): "))
    if r < 0 or r > 100:
        print("Ingresa un valor positivo para las filas")
    else:
        break
while True:
    c:int = int(input("Ingresa el valor de m (columnas): "))
    if c < 0 or c > 100:
        print("Ingresa un valor positivo para las columnas")
    else:
        break

# Impresión de matriz
for i in range(r):
    for j in range(c):
        s += m[i][j]
        print(f"{m[i][j]}", end = " ")
    print()

print(f"La suma de los elementos es: {s}")