import requests
from bs4 import BeautifulSoup

def capturar_tareas(url):
    # Realizar la solicitud HTTP
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código 200)
    if response.status_code == 200:
        # Analizar el contenido HTML de la página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Aquí puedes buscar y capturar las tareas según la estructura HTML de la página
        # Por ejemplo, si las tareas están en elementos con la clase 'tarea':
        tareas = soup.find_all(class_='tarea')

        # Procesar las tareas capturadas
        for tarea in tareas:
            print(tarea.text)
    else:
        print(f"No se pudo acceder a la página. Código de estado: {response.status_code}")

# Ejemplo de uso
url_pagina = 'https://www.youtube.com'
capturar_tareas(url_pagina)