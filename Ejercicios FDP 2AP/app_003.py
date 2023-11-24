# Ejercicio 3: Obtenga el promedio de n números positivos leidos del teclado
# Christian David Sánchez Sánchez 1°B
from guizero import App, Text, TextBox, PushButton

numeros = 0
cant = 0
def agregar_numero():
    global numeros, cant
    numero = valor.value
    try:
        numero = float(numero)
        if numero > 0:
            numeros = numeros + numero
            cant = cant + 1
            valor.clear()
        else:
            app.error(title="Error", text="Ingresa un número positivo")
    except ValueError:
        app.error(title="Error", text="Ingresa un número válido")

def calcular_promedio():
    if numeros:
        resultado = float(numeros / cant)
        app.info(title="Resultado", text=f"El promedio es: {resultado}")
    else:
        app.error(title="Error", text="No se ingresaron números")

app = App(title="Promedio de n numeros positivos")
message = Text(app, text="Ingresa números positivos")
valor = TextBox(app, width=20)
button1 = PushButton(app, text="Agregar número", command=agregar_numero)
button2 = PushButton(app, text="Calcular el promedio", command=calcular_promedio)

app.display()