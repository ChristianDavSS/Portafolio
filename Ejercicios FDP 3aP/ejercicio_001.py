# Ejercicio 1: Haz las modificaciones para verificar las veces que se repite un número en el array.
# Christian David Sánchez Sánchez
array = [1, 3, 5, 7, 9, 11]

numero_a_buscar = 3
c = 0

for i in range(len(array)):
    if array[i] == numero_a_buscar:
        c += 1

print(f"El número {numero_a_buscar} se repite {c} veces en la matriz.")