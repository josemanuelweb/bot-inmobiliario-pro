from flask import Flask, render_template, send_from_directory
import os

# Configuramos Flask para que busque el index en la raíz '.' 
# en lugar de la carpeta 'templates'
app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

# Ruta para que la web pueda leer el JSON y el Excel
@app.route('/<path:path>')
def send_file(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True)