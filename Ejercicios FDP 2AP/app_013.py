# Ejercicio 13: Generar la serie 0, 1, 0, 1... INFINITAMENTE
# Christian David Sánchez Sánchez 1°B
from guizero import App, Text, TextBox, PushButton

c = 0
def secuencia():
    global c
    while True:
        app.info(title="Resultado", text=f"{c}")
        c += 1
        app.info(title="Resultado", text=f"{c}")
        c -= 1

app = App(title="Generar la serie de 0, 1 infinitamente")
message = Text(app,text="Presiona el botón de abajo para generar la secuencia infinitamente")
boton = PushButton(app, text="Presioname", command = secuencia)

app.display()