# Ejercicio 1: Obtenga el promedio de 3 numeros cualquiera.
# Christian David Sánchez Sánchez 1°B
from guizero import App, Text, PushButton

def promedio_numeros():
    promedio = int(10 + 8 + 6) / 3
    cadena = str(promedio)
    app.info(title="Resultado", text=f"El promedio de 10, 8 y 6 es: {cadena}")

app = App(title="Obtener el promedio de 3 numeros cualquiera")

message = Text(app,text="Obtener el promedio de 10, 8 y 6")
button = PushButton(app, text="Obtener promedio", command = promedio_numeros)

app.display()