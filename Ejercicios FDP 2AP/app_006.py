# Ejercicio 6: Calcule el cuadrado de un número positivo leido del teclado.
# Christian David Sánchez Sánchez 1°B
from guizero import App, Text, TextBox, PushButton

def cuadrado():
    numero = number.value
    try:
        numero = int(numero)
        if numero > 0:
            resultado = numero ** 2
            app.info(title="Resultado", text=f"El cuadrado del número es: {resultado}")
        else:
            app.error(title="Error", text="Ingresa un numero positivo")
    except ValueError:
        app.error(title="Error", text="Ingresa un número")

app= App(title="Calcula el cuadrado de un numero positivo")
message = Text(app,text="Ingresa el número")
number = TextBox(app,width=30)
button = PushButton(app,text="Calcular cuadrado", command = cuadrado)

app.display()