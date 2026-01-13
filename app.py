from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

# Esta ruta permite que el navegador descargue el JSON y el Excel
@app.route('/<path:path>')
def send_file(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    # Usamos el puerto que pide Render por defecto
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)