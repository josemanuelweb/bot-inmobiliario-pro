from flask import Flask, render_template
import json
import os

app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/')
def index():
    datos = []
    try:
        if os.path.exists('propiedades.json'):
            with open('propiedades.json', 'r', encoding='utf-8') as f:
                datos = json.load(f)
    except Exception as e:
        print(f"Error leyendo JSON: {e}")

    # --- Lógica de Marketing ---
    # Mostramos solo las primeras 4 en la web para mantener el diseño limpio
    # y que el usuario sienta que hay mucho más contenido en el reporte full.
    datos_web = datos[:4] 

    return render_template('index.html', propiedades=datos_web)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)