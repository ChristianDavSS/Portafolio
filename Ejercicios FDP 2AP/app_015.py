# Ejercicio 15: Preguntar un número y determinar que dia de la semana es.
# Christian David Sánchez Sánchez 1°B
from guizero import App, Text, TextBox, PushButton

def dia():
    num = numero.value
    try:
        num = int(num)
        if num >= 1 and num <= 7:
            match(num):
                case (1):
                    app.info(title="Resultado", text="Lunes")
                case (2):
                    app.info(title="Resultado", text="Martes")
                case (3):
                    app.info(title="Resultado", text="Miercoles")
                case (4):
                    app.info(title="Resultado", text="Jueves")
                case (5):
                    app.info(title="Resultado", text="Viernes")
                case (6):
                    app.info(title="Resultado", text="Sabado")
                case (7):
                    app.info(title="Resultado", text="Domingo")
        else:
            app.error(title="Error", text="Ingresa un número del rango")

    except ValueError:
        app.error(title="Error", text="Ingresa un valor valido")

app = App(title="Determinar que dia de la semana es con base a un número")
message = Text(app, text="Ingresa un número entre 1 y 7")
numero = TextBox(app,width=30)
boton = PushButton(app, text="Determinar dia de la semana", command = dia)

app.display()