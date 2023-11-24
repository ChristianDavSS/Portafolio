# Ejercicio 11: Obtenga la suma de 5 numeros capturados entre [5, 10].
# Christian David Sánchez Sánchez 1°B
from guizero import App, Text, TextBox, PushButton

i = 1
sum = 0
def numeros():
    global i, sum
    num = numero.value
    try:
        num = float(num)
        if num >= 5 and num <= 10:
            sum += num
            if i < 5:
                i += 1
                numero.clear()
            else:
                app.info(title="Resultado", text=f"La suma de los 5 números es: {sum}")
        else:
            app.error(title="Error", text="Ingresa un número dentro del rango")
    except ValueError:
        app.error(title="Error", text="Ingresa un valor")

app = App(title="Suma de números capturados entre [5, 10]")
message = Text(app,text="Ingresa un número")
numero = TextBox(app,width=30)
button = PushButton(app, text="Agregar número", command= numeros)

app.display()