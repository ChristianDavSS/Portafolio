# Ejercicio 5: Se desea saber la cantidad de alumnos que pasaron una materia son 25 y la calificacion aprobatoria es 7.
# Christian David Sánchez Sánchez 1°B
from guizero import App, Text, TextBox, PushButton

c_alumnos = 25
ia = 0
i = 0
def calculo():
    global ia, i, c_alumnos
    cal = calificacion.value
    try:
        cal = float(cal)
        if cal <= 10 and cal >= 0:
            i += 1
            calificacion.clear()
            if cal >= 7:
                ia += 1
            if i == c_alumnos:
                app.info(title="Resultado", text=f"Alumnos aprobados: {ia}")
        else:
            app.error(title="Error", text="Ingresa un numero entre 0 y 10")
    except ValueError:
        app.error(title="Error", text="Ingresa un número")

app = App(title="Obtener la cantidad de alumnos que pasaron una materia")
message = Text(app, text="Ingresa la calificación de 25 alumnos")
calificacion = TextBox(app,width=30)
button1 = PushButton(app, text="Agregar calificación", command = calculo)

app.display()