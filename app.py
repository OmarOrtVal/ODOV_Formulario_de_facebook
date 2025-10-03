from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file("formulario.html")

@app.route('/registrar/<nombre>/<apellido>/<contacto>/<genero>/<fecha>/<contrasena>')
def registrar(nombre, apellido, contacto, genero, fecha, contrasena):
    print("--- Nuevo Registro ---")
    print(f"Nombre: {nombre} {apellido}")
    print(f"Contacto: {contacto}")
    print(f"Fecha de Nacimiento: {fecha}")
    print(f"Género: {genero}")
    print(f"Contraseña: {contrasena}")
    print("----------------------")

    return f"""
    <h2>¡Registro exitoso!</h2>
    <p><b>Nombre:</b> {nombre} {apellido}</p>
    <p><b>Contacto:</b> {contacto}</p>
    <p><b>Fecha de Nacimiento:</b> {fecha}</p>
    <p><b>Género:</b> {genero}</p>
    <p><b>Contraseña:</b> {contrasena}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
