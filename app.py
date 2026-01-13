from flask import Flask, render_template
import json
import os

app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/')
def index():
    # Leemos el JSON directamente desde Python
    try:
        with open('propiedades.json', 'r', encoding='utf-8') as f:
            datos = json.load(f)
    except Exception as e:
        print(f"Error leyendo JSON: {e}")
        datos = []

    # Enviamos los datos a la web
    return render_template('index.html', propiedades=datos)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)