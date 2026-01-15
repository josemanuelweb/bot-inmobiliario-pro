import cloudscraper
import pandas as pd
import json
from bs4 import BeautifulSoup

def hacer_scraping():
    # Configuración del "disfraz" para saltar bloqueos
    scraper = cloudscraper.create_scraper(
        browser={
            'browser': 'chrome',
            'platform': 'windows',
            'desktop': True
        }
    )
    
    url = "https://www.zonaprop.com.ar/departamentos-alquiler-capital-federal-dueno-directo-orden-publicado-descendente.html"
    
    print("🚀 Iniciando búsqueda de oportunidades reales...")
    
    resultados = []

    try:
        response = scraper.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            propiedades = soup.find_all('div', {'data-qa': 'posting PROPERTY'})
            
            for prop in propiedades:
                try:
                    enlace = prop.find('a', href=True)
                    if not enlace or '/propiedades/' not in enlace['href']:
                        continue
                        
                    link_final = "https://www.zonaprop.com.ar" + enlace['href']
                    precio = prop.find(attrs={"data-qa": "POSTING_CARD_PRICE"}).text.strip()
                    ubicacion = prop.find(attrs={"data-qa": "POSTING_CARD_LOCATION"}).text.strip()
                    titulo = prop.find('h3').text.strip()

                    resultados.append({
                        "Barrio": ubicacion,
                        "Precio": precio,
                        "Descripcion": titulo,
                        "Link": link_final
                    })
                except:
                    continue
            
    except Exception as e:
        print(f"❌ Error en la conexión: {e}")

    # --- PROCESAMIENTO Y LIMPIEZA ---
    if resultados:
        df = pd.DataFrame(resultados)
        
        # Filtro de Calidad: Eliminamos duplicados basados en el contenido
        # (Si el barrio, precio y descripción son iguales, es la misma propiedad)
        total_sucios = len(df)
        df = df.drop_duplicates(subset=['Barrio', 'Precio', 'Descripcion'], keep='first')
        total_limpios = len(df)
        
        print(f"🔥 ¡ÉXITO! Se capturaron {total_sucios} avisos.")
        print(f"✨ Limpieza completada: Se eliminaron {total_sucios - total_limpios} repetidos.")
        
        # Guardar JSON para la web
        resultados_limpios = df.to_dict(orient='records')
        with open('propiedades.json', 'w', encoding='utf-8') as f:
            json.dump(resultados_limpios, f, indent=4, ensure_ascii=False)
        
        # Guardar Excel para el cliente
        df.to_excel('Reporte_Oportunidades_InmoData.xlsx', index=False)
        print("✅ Reporte_Oportunidades_InmoData.xlsx generado y limpio.")
    else:
        print("⚠️ No se encontraron resultados nuevos. Verifica el sitio o el respaldo.")

if __name__ == "__main__":
    hacer_scraping()