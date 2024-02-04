# Ejercicio 3: Indique la cantidad de veces que se repite un determinado
# número en una matriz de nxm, así como las posiciones donde se repite.
# Christian David Sánchez Sánchez 1°B
import random

renglones = 100
columnas = 100
repeticiones = 0
m = [[(random.randint(1,100)) for _ in range(columnas)]for _ in range(renglones)]

while True:
    r:int = int(input("Ingresa n: "))
    if r <= 0 or r > 100:
        print("Ingresa un número de n valido")
    else:
        break
while True:
    c:int = int(input("Ingresa m: "))
    if c <= 0 or c > 100:
        print("Ingresa un número de m valido")
    else:
        break

# Número a buscar
while True:
    buscar:int = int(input("Ingresa el número a buscar: "))
    if buscar < 0:
        print("El número ingresado es negativo")
    else:
        break
print()

#Impresion de la matriz
for i in range(r):
    for j in range(c):
        print(f"{m[i][j]}", end= " ")
    print()
print()

# Impresión de resultados
for i in range(r):
    for j in range(c):
        if m[i][j] == buscar:
            print(f"El número {buscar} se encuentra en: [{i}, {j}]")
            repeticiones += 1

print(f"El número {buscar} fue repetido {repeticiones} veces")