# Ejercicio 2: Modifica el programa para que en vez de decirte si el número está o no
# dentro del array, te diga cuantas veces se repite el número y en que posiciones lo hace.
# Christian David Sánchez Sánchez 1°B
array = [1, 3, 5, 7, 9, 11]
num = 5
c = 0

resultado = "El número no está en la matriz"

for i in range(len(array)):
    if array[i] == num:
            c += 1
            resultado = ""
            print(f"El número {num} está en [0, {i}]")

print(f"{resultado}")
print(f"Se repite {c} veces")