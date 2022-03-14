
'''Script para convertir WORD (.docx) a PDF'''

import convertapi
import os

API_KEY = os.environ['APIKEY_CONVERTAPI']
convertapi.api_secret = API_KEY

file = os.path.join(os.path.dirname(__file__), '../test_word.docx')
result_folder = os.path.join(os.path.dirname(__file__), '../results/')

result = convertapi.convert('pdf', { 'File': file })

# save to file
result.save_files(result_folder)
print("Archivo guardado en la carpeta: " + result_folder)
