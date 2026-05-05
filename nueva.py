import requests
from PIL import Image
from io import BytesIO

# URL de la API
URL = "https://api.nasa.gov/planetary/apod"

# Parámetros (agregamos la fecha que quieres)
params = {
    "api_key": "DEMO_KEY",
    "date": "2022-12-12"
}

# Hacer la petición
response = requests.get(URL, params=params)
data = response.json()

# Mostrar info
print("Fecha:", data["date"])
print("Título:", data["title"])
print("Descripción:", data["explanation"])

# Obtener y mostrar la imagen
img_url = data["url"]
img_response = requests.get(img_url)

img = Image.open(BytesIO(img_response.content))
img.show()