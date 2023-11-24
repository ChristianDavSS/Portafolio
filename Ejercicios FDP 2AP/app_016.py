# Ejercicio 16: Productos totales vendidos por Branko´s a n alumnos.
# Christian David Sánchez Sánchez 1°B
from guizero import App, Text, TextBox, PushButton

c1 = 0
c2 = 0
c3 = 0
c4 = 0
def orden():
    global c1, c2, c3, c4
    pedido = numero.value
    try:
        pedido = int(pedido)
        if pedido >= 1 and pedido <= 4:
            match (pedido):
                case (1):
                    c1 += 1
                case (2):
                    c2 += 1
                case (3):
                    c3 += 1
                case (4):
                    c4 += 1
            numero.clear()
        else:
            app.error(title="Error", text="Ingresa un número de pedido disponible")
    except ValueError:
        app.error(title="Error", text="Ingresa un valor valido")

def resultado():
    suma = c1 + c2 + c3 + c4
    app.info(title="Resultado", text=f"Brankos vendió {suma} productos en total")

app = App(title="Calcular los productos que vendió en total Brankos a n alumnos")
message = Text(app, text="El menú es: \n1.- Tortas \n2.- Tacos \n3.- Hot-Dogs \n4.- Pizza")
message = Text(app, text="¿Que desea ordenar?")
numero = TextBox(app,width=30)
button1 = PushButton(app,text="Agregar orden", command = orden)
button2 = PushButton(app,text="Productos vendidos en total", command = resultado)

app.display()