import json
import pandas as pd
import os

def hacer_scraping():
    # Aquí es donde tu bot pone los links que encuentra
    resultados = [
        {
            "titulo": "Depto 2 Amb. Palermo", 
            "barrio": "Palermo", 
            "precio": "USD 92.000", 
            "link": "https://www.zonaprop.com.ar/propiedades/ejemplo-palermo-1.html"
        },
        {
            "titulo": "Monoambiente Recoleta", 
            "barrio": "Recoleta", 
            "precio": "USD 68.500", 
            "link": "https://www.zonaprop.com.ar/propiedades/ejemplo-recoleta-2.html"
        }
    ]
    
    # Guardar JSON para la Web
    with open('propiedades.json', 'w') as f:
        json.dump(resultados, f, indent=4)
    
    # Guardar Excel para el Cliente (Con columna de links)
    df = pd.DataFrame(resultados)
    df.to_excel('Reporte_Oportunidades_InmoData.xlsx', index=False)
    
    print("¡Base de datos y Excel generados con éxito!")

if __name__ == "__main__":
    hacer_scraping()