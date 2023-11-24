# Ejercicio 8: Obtenga la suma de todos los cuadrados de n números capturados del teclado.
# Christian David Sánchez Sánchez 1°B
from guizero import App, Text, TextBox, PushButton

suma = 0
def calculos():
    global suma
    num = numero.value
    try:
        num = float(num)
        if num > 0:
            suma = suma + (num**2)
            numero.clear()
        else:
            app.error(title="Error", text="Ingresa un numero positivo")
    except ValueError:
        app.error(title="Error", text="Ingresa un valor")

def resultado():
    app.info(title="Resultado", text=f"La suma de los cuadrados es: {suma}")
app = App(title="Suma de los cuadrados de n numeros capturados del teclado")
message = Text(app, text="Ingresa un número")
numero = TextBox(app, width=30)
button1 = PushButton(app, text="Agregar su cuadrado", command = calculos)
button2 = PushButton(app, text="Obtener la suma de los cuadrados", command = resultado)

app.display()