
'''Script para extraer imagenes de PDF con la API de ConvertAPI'''

import convertapi
import os

API_KEY = os.environ['APIKEY_CONVERTAPI']

file = os.path.join(os.path.dirname(__file__), '../test_img.pdf')
result_folder = os.path.join(os.path.dirname(__file__), '../results/')

convertapi.api_secret = API_KEY

print("Convirtiendo el archivo: " + file)
result = convertapi.convert('extract-images', {'File': file}, from_format = 'pdf')

result.save_files(result_folder)
print("Archivo guardado en la carpeta: " + result_folder)
