# Ejercicio 10: Dado el año de nacimiento indique cuantos años cumplirá una persona el año siguiente.
# Christian David Sánchez Sánchez 1°B
from guizero import App, Text, TextBox, PushButton

año = 2023

def año_siguiente():
    global año
    nacimiento = a_nac.value
    try:
        nacimiento = int(nacimiento)
        if nacimiento < año and nacimiento > 0:
            edad = año - nacimiento + 1
            app.info(title="Resultado", text=f"La edad que tendrás el año que viene es: {edad}")
        else:
            app.error(title="Error", text="Ingresa un número valido")
    except ValueError:
        app.error(title="Error", text="Ingresa un número")

app = App(title="Calcular que edad cumplirá el año siguiente")
message = Text(app,text="Ingresa tu año de nacimiento")
a_nac = TextBox(app, width=30)
button = PushButton(app,text="Calcular", command = año_siguiente)

app.display()