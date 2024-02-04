# Ejercicio 5: Implementa un algoritmo que invierta los elementos de un array de tamaño n dado.
# Christian David Sánchez Sánchez
import random

array = [(random.randint(1,50))for _ in range(100)]

while True:
    num:int = int(input("Ingresa el tamaño del array: "))
    if num < 0 or num > 100:
        print("Ingresa un número valido")
    else:
        break

inicio = 0
fin = num - 1

print("El array original es:")
for i in range(num):
    print(f"{array[i]}", end= " ")
print()
while inicio < fin:
    aux = array[inicio]
    array[inicio] = array[fin]
    array[fin] = aux

    inicio += 1
    fin -= 1

print("El array invertido es:")
for i in range(num):
    print(f"{array[i]}", end= " ")
print()