# Importamos Flask y los módulos necesarios
from flask import Flask, request, render_template

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Definimos la ruta principal ("/") que acepta solicitudes GET
@app.route("/", methods=["GET"])
def hello():
    # Obtiene el parámetro 'name' desde la URL (ejemplo: ?name=Luis)
    # Si no se proporciona un nombre, usa "Invitado" por defecto
    name = request.args.get("name", "Invitado")  
    
    # Renderiza la plantilla HTML 'index.html' y pasa la variable 'name'
    return render_template("index.html", name=name)

# Ejecutamos la aplicación solo si este archivo es el principal
if __name__ == "__main__":
    # Inicia el servidor Flask en el puerto 8080
    # 'host="0.0.0.0"' permite acceder desde cualquier dispositivo en la red
    # 'debug=True' activa el modo depuración para mostrar errores en la terminal
    app.run(host="0.0.0.0", port=8080, debug=True)
