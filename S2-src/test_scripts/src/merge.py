
'''Script para combinar 2 PDF con la API de ConvertAPI'''

import convertapi
import os

API_KEY = os.environ['APIKEY_CONVERTAPI']

path1 = os.path.join(os.path.dirname(__file__), '../file1.pdf')
path2 = os.path.join(os.path.dirname(__file__), '../file2.pdf')
result_folder = os.path.join(os.path.dirname(__file__), '../results/')

files = [path1, path2]

convertapi.api_secret = API_KEY

print(f"Convirtiendo los archivos: {files[0]}, {files[1]}")
result = convertapi.convert('merge', {'Files': files}, from_format = 'pdf')

result.file.save(result_folder + 'my_file.pdf')
print("Archivo guardado en: " + result_folder)
