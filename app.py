from flask import Flask, render_template, send_from_directory
import os

# Configuramos para que busque todo en la carpeta principal
app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

# Ruta crucial para que el cliente pueda descargar archivos
@app.route('/<path:path>')
def send_file(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)