# Ejercicio 2: Calcular la edad de una persona dados el año de nacimiento y actual.
# Christian David Sánchez Sánchez 1°B
from guizero import App, Text, TextBox, PushButton

def edad():
    nacim = año_nac.value
    actual = año_act.value
    try:
        nacim = int(nacim)
        actual = int(actual)
        if nacim < actual and nacim > 0:
            edad = actual - nacim
            app.info(title="Resultado", text=f"Tu edad es: {edad}")
        else:
            app.error(title="Error", text="Escribe un número valido")
    except ValueError:
        app.error(title="Error", text="Ingresa un número valido")

app = App(title="Obtener la edad de una persona dado el año de nacimiento y actual")

message = Text(app,text="Ingresa el año actual")
año_act = TextBox(app,width=30)
message = Text(app,text="Ingresa el año de nacimiento")
año_nac = TextBox(app,width=30)

button = PushButton(app,text="Obtener la edad", command = edad)

app.display()