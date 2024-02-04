# Programa para calcular promedios de 37 alumnos siendo 7 materias.
# Inicializar variables
mat = 7
alu = 37
m = [[0 for _ in range(mat)] for _ in range(alu)]
pm = [0, 0, 0, 0, 0, 0, 0]
pa = [0 for _ in range(alu)]
c_alum = 0

#Llenado de matriz
for i in range(alu):
    c = 1
    c_alum += 1
    for j in range(mat):
        while True:
            n:int = float(input(f"Ingresa la calificación {c} del alumno {c_alum}: "))
            if n < 0 or n > 10:
                print("Error en la calificación ingresada")
            else:
                m[i][j] = n
                c += 1
                break #Se rompe el while solamente, veulve a entrar gracias al for.

#Calcular los promedios
for i in range(alu):
    for j in range(mat):
        pm[j] = pm[j] + (m[i][j] / alu)
        pa[i] = pa[i] + (m[i][j] / mat)

#Impresión de resultados
c = 1
for i in range(alu):
    print(f"El promedio del alumno {c} es de {pa[i]}")
    c += 1

c = 1
for j in range(mat):
    print(f"El promedio de la materia {c} es de {pm[j]}")
    c += 1