from flask import Flask, render_template, send_file
import pandas as pd
import requests
from bs4 import BeautifulSoup
import io

app = Flask(__name__)

# Función de Scraping (Simulada para un portal estándar)
def ejecutar_scraping():
    # Ejemplo con un buscador (puedes cambiar la URL por una de Zonaprop/Argenprop)
    url = "https://www.argenprop.com/departamentos-alquiler-localidad-capital-federal"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        propiedades = []
        # Buscamos los contenedores de las propiedades (este selector es clave)
        items = soup.select(".listing__item") # Selector común en Argenprop
        
        for item in items[:20]: # Limitamos a 20 para ir rápido
            precio = item.select_one(".card__price").text.strip() if item.select_one(".card__price") else "Consultar"
            info = item.select_one(".card__title").text.strip() if item.select_one(".card__title") else "Sin descripción"
            
            propiedades.append({
                'Descripcion': info,
                'Precio': precio,
                'Fuente': 'Argenprop'
            })
        
        return pd.DataFrame(propiedades)
    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame([{"Error": "No se pudo extraer data"}])

@app.route('/')
def index():
    # Simulamos el scraping real de 3 propiedades para la vista previa
    # En el futuro, aquí llamarás a tu función de BeautifulSoup
    muestra_gratis = [
        {'titulo': 'Depto 2 Amb. Palermo', 'precio': 'USD 95.000', 'barrio': 'Palermo'},
        {'titulo': 'Monoambiente Recoleta', 'precio': 'USD 72.000', 'barrio': 'Recoleta'},
        {'titulo': 'Casa 3 Amb. Olivos', 'precio': 'USD 215.000', 'barrio': 'Olivos'}
    ]
    return render_template('index.html', propiedades=muestra_gratis)

@app.route('/descargar')
def descargar():
    df = ejecutar_scraping()
    
    # Guardamos en un buffer de memoria para no crear archivos basura
    buffer = io.BytesIO()
    df.to_csv(buffer, index=False, encoding='utf-8')
    buffer.seek(0)
    
    return send_file(
        buffer,
        mimetype='text/csv',
        download_name='reporte_inmobiliario.csv',
        as_attachment=True
    )

if __name__ == '__main__':
    # Cambiamos a 0.0.0.0 para que sea accesible y cambiamos el puerto al 8080
    app.run(debug=True, host='0.0.0.0', port=8080)