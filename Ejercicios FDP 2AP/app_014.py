# Ejercicio 14: Generar la serie 0, 1, 0, 1... FINITAMENTE
# Christian David Sánchez Sánchez 1°B
from guizero import App, Text, TextBox, PushButton

num = 0
i = 0
def secuencia():
    global i, num
    numeros = cantidad.value
    try:
        numeros = int(numeros)
        while i < numeros:
            app.info(title="Resultado", text=f"{num}")
            i += 1
            num += 1
            if i < numeros:
                app.info(title="Resultado", text=f"{num}")
                i += 1
                num -= 1
    except ValueError:
        app.error(title="Error", text="Ingresa un valor valido")

app = App(title="Generar la serie de 0, 1 de forma finita")
message = Text(app,text="¿Cuantos numeros quieres en la secuencia?")
cantidad = TextBox(app,width=30)
boton = PushButton(app, text="Generar secuencia", command = secuencia)

app.display()