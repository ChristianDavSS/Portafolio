# Ejercicio 12: Una empresa desea calcular el sueldo de una persona bajo rubros.
# Christian David Sánchez Sánchez 1°B
from guizero import App, Text, TextBox, PushButton

s = 0
i1 = 0
i2 = 0
def calculos():
    global s, i1, i2
    sb = base.value
    try:
        sb = float(sb)
        if sb > 0:
            percep_1 = sb * .05
            percep_2 = sb * .03
            s_percep = percep_1 + percep_2 + sb
            s = s + s_percep
            base.clear()
            if sb < 10000:
                i1 = i1 + (s_percep * .20)
            else:
                i2 = i2 + (s_percep * .30)
        else:
            app.error(title="Error", text="Ingresa un sueldo valido")
    except ValueError:
        app.error(title="Error", text="Ingresa un valor")

def resultado():
    if s > 0:
        app.info(title="Nómina a pagar", text=f"La nómina a pagar es: {s}")
        app.info(title="Impuestos a pagar al SAT", text=f"Los impuestos a pagar al SAT son: {i1 + i2}")
    else:
        app.error(title="Error", text="Ingresa cantidades")

app = App(title="Calcular el sueldo de una persona con percepciones junto a impuestos")
message = Text(app, text="Ingresa el sueldo base")
base = TextBox(app, width=30)
button1 = PushButton(app, text ="Calcular percepciones y agregar sueldo", command = calculos)
button2 = PushButton(app, text ="Resultados", command = resultado)

app.display()