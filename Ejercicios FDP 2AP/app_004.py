# Ejercicio 4: Obtener la edad promedio de n personas preguntando su año de nacimiento y asumiendo que es 2023.
# Christian David Sánchez Sánchez 1°B
from guizero import App, Text, TextBox, PushButton

personas = 0
edades = 0

def agregar_año():
    global personas, edades
    año = años.value
    try:
        año = int(año)
        if año < 2023 and año > 0:
            edad = 2023 - año
            personas = personas + 1
            edades = edades + edad
            años.clear()
        else:
            app.error(title="Error", text="Ingresa un año de nacimiento valido")
    except ValueError:
        app.error(title="Error", text="Ingresa un número valido")

def promedio():
    if edades > 0:
        promedio = float(edades/personas)
        app.info(title="Resultado", text=f"El promedio es: {promedio}")
    else:
        app.error(title="Error", text="No ingresaste numeros")

app = App(title="Obtener la edad promedio de n personas preguntando su año de nacimiento")
message = Text(app, text="Ingresa tu año de nacimiento")
años = TextBox(app,width=30)
button1 = PushButton(app, text="Agregar año", command = agregar_año)
button2 = PushButton(app,text="Obtener promedio", command = promedio)

app.display()