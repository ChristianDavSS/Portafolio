# Ejercicio 7: Desarrolla un algoritmo que determine si una matriz dada es una matriz identidad. Una matriz identidad
# es una matriz cuadrada en la que todos los elementos de la diagonal principal son 1 y el resto son 0.
# Christian David Sánchez Sánchez 1°B
matriz = [[1, 0, 0, 0, 0],
          [0, 1, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 1, 0],
          [0, 0, 0, 0, 1]]
TAM = 5
resultado = "Es una matriz identidad"

for i in range(TAM):
    for j in range(TAM):
        if i == j and matriz[i][j] == 0:
            resultado = "No es una matriz identidad"
        elif i != j and matriz[i][j] == 1:
            resultado = "No es una matriz identidad"

print(resultado)