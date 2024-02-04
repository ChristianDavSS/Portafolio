matrix = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]
vc = [0, 0, 0, 0]
vr = [0, 0, 0, 0]
TAM = 4
c = 1
def limpiar_matriz(TAM):
    for i in range(TAM):
        for j in range (TAM):
            matrix[i][j] = 0
def imprimir(TAM):
    for i in range(TAM):
        for j in range(TAM):
            print(f"{matrix[i][j]}", end = " ")
        print()

limpiar_matriz(TAM)

#LLENADO DE MATRIZ
for i in range(TAM):
    for j in range(TAM):
        while True:
            num:int = int(input(f"Ingresa el número {c} a agregar: "))
            if num < 0:
                print("El número ingresado no es valido")
            else:
                matrix[i][j] = num
                c += 1
                break

for i in range(TAM):
    for j in range(TAM):
        vr[i] = vr[i] + matrix[i][j]
        vc[j] = vc[j] + matrix[i][j]

imprimir(TAM)
print(f"COLUMNAS: {vc[0], vc[1], vc[2], vc[3]}")
print(f"RENGLONES: {vr[0], vr[1], vr[2], vr[3]}")