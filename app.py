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

    # --- Lógica de balance visual ---
    # Si hay menos de 4, agregamos de respaldo para que la web se vea llena
    respaldo = [
        {"Barrio": "Palermo", "Precio": "USD 125.000", "Descripcion": "2 Amb - Oportunidad Única", "Link": "#"},
        {"Barrio": "Recoleta", "Precio": "USD 98.000", "Descripcion": "Ideal Inversión / AirBnb", "Link": "#"},
        {"Barrio": "Belgrano", "Precio": "USD 115.000", "Descripcion": "Dueño directo impecable", "Link": "#"},
        {"Barrio": "Caballito", "Precio": "USD 89.000", "Descripcion": "3 Ambientes luminoso", "Link": "#"}
    ]

    # Si faltan datos, completamos con los de respaldo hasta llegar a 4
    if len(datos) < 4:
        faltantes = 4 - len(datos)
        datos.extend(respaldo[:faltantes])

    return render_template('index.html', propiedades=datos)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)