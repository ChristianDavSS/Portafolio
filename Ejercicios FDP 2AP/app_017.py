# Ejercicio 17: Crea el menú de una calculadora funcional que pueda hacer operaciones basicas al dar 2 valores.
# Christian David Sánchez Sánchez 1°B
from guizero import App, Text, TextBox, PushButton

s1 = 0
s2 = 0

def calculo():
    num1 = numero1.value
    num2 = numero2.value
    operacion = procedimiento.value
    try:
        num1 = float(num1)
        num2 = float(num2)
        operacion = float(operacion)
        if operacion >= 1 and operacion <= 4:
            match (operacion):
                case(1):
                    app.info(title="Suma", text=f"La suma entre {num1} y {num2} es: {num1 + num2}")
                case (2):
                    app.info(title="Resta", text=f"La resta entre {num1} y {num2} es: {num1 - num2}")
                case (3):
                    app.info(title="Multiplicación", text=f"La multiplicación entre {num1} y {num2} es: {num1 * num2}")
                case (4):
                    app.info(title="Division", text=f"La resta entre {num1} y {num2} es: {num1 / num2}")
        else:
            app.error(title="Error", text="Ingresa un número del rango")

    except ValueError:
        app.error(title="Error", text="Ingresa un valor valido")
    

app = App(title="Calculadora funcional")
message = Text(app, text="Ingresa el primer valor")
numero1 = TextBox(app,width=30)
message = Text(app, text="Ingresa el segundo valor")
numero2 = TextBox(app,width=30)
message = Text(app,text="¿Que operación quiere realizar?")
message= Text(app, text="Operaciones: \n1.- Suma \n2.- Resta \n3.- Multiplicación \n4.- División")
procedimiento = TextBox(app,width=30)
button2 = PushButton(app, text="Realizar operación", command= calculo)

app.display()