#importamos Flask y las herramientas necesarias para crear y
# mostrar paginas HTML
from flask import Flask, render_template, request

#creamos la aplicacion flask
app = Flask(__name__)


#definimos la ruta principal de la aplicacion.
@app.route('/')
def index():
    #mostramos la pagina principal del proyecto
    return render_template('index.html')



#Definimos la ruta para el ejercicio 1.
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():

    #comprobamos si se enviaron los datos del formulario
    if request.method == 'POST':

        #obtenemos las notas ingresadas por el usuario
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])

        #obtenemos el porcentaje de asistencia
        asistencia = int(request.form['asistencia'])

        #Calculamos el promedio de notas
        promedio= (nota1+nota2+nota3)/3

        #comprobamos si el estudiante cumple los requisitos
        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        #enviamos los resultados a la pagina HTML
        return render_template('ejercicio1.html',promedio=promedio, estado=estado)
    return render_template('ejercicio1.html')



#Definimos la ruta para el ejercicio 2.
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():

    #Comprobamos si se enviaron los datos del formulario
    if request.method == 'POST':

        #Obtenemos los tres nombres ingresados
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        #Contamos la cantidad de caracteres de cada nombre
        cantidad1=len(nombre1)
        cantidad2=len(nombre2)
        cantidad3=len(nombre3)

        #Comparamos la cantidad de caracteres
        if cantidad1 >= cantidad2  and cantidad1 >= cantidad3:
            nombre_mayor = nombre1
            cantidad = cantidad1

        elif cantidad2 >= cantidad1 and cantidad2 >= cantidad3:
            nombre_mayor = nombre2
            cantidad = cantidad2

        else:
            nombre_mayor = nombre3
            cantidad = cantidad3

        #Enviamos los resultados a la pagina HTML
        return render_template('ejercicio2.html', nombre_mayor=nombre_mayor, cantidad=cantidad)
    return render_template('ejercicio2.html')


#comprobamos que el archivo se ejecute directamente
if __name__ == '__main__':
    #iniciamos el servidor en modo depuracion
    app.run(debug=True)

