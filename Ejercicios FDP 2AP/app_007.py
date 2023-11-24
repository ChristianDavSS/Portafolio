# Ejercicio 7: Imprime los numeros pares entre 0 y 20.
# Christian David Sánchez Sánchez 1°B
from guizero import App, Text, PushButton

num = 2
def pares():
    global num
    while num <= 20:
        app.info(title="Resultado", text=f"{num}")
        num = num + 2

app = App(title="Imprimir los numeros pares entre 0 y 20")
message = Text(app,text="Presiona para imprimir los numeros pares entre 0 y 20")
button = PushButton(app,text="Presiona", command = pares)

app.display()