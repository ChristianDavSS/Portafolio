# Ejercicio 9: Capture n números enteros positivos, obtenga la suma del cuadrado de los pares y el cubo de los impares.
# Christian David Sánchez Sánchez 1°B
from guizero import App, Text, TextBox, PushButton

suma_pares = 0
suma_impares = 0
def calculos():
    global suma_pares, suma_impares
    num = numero.value
    try:
        num = int(num)
        if num > 0:
            numero.clear()
            if num % 2 == 0:
                suma_pares = suma_pares + (num**2)
            else:
                suma_impares = suma_impares + (num**3)
        else:
            app.error(title="Error", text="Ingresa un numero positivo")
    except ValueError:
        app.error(title="Error", text="Ingresa un valor valido")

def resultado():
    app.info(title="Resultado", text=f"La suma de los cuadrados de los pares es: {suma_pares}")
    app.info(title="Resultado", text=f"La suma del cubo de los impares es: {suma_impares}")

app = App(title="Obtenga la suma del cuadrado de los pares y cubo de impares")
message = Text(app, text="Ingresa un número")
numero = TextBox(app, width=30)
button1 = PushButton(app, text="Agregar su cuadrado", command = calculos)
button2 = PushButton(app, text="Obtener las sumas", command = resultado)

app.display()