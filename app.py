from flask import Flask, render_template
import json
import os

app = Flask(__name__)

def cargar_propiedades():
    # Si el archivo existe, lo lee; si no, devuelve una lista vacía
    if os.path.exists('propiedades.json'):
        with open('propiedades.json', 'r') as f:
            return json.load(f)
    return []

@app.route('/')
def index():
    datos = cargar_propiedades()
    return render_template('index.html', propiedades=datos)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)