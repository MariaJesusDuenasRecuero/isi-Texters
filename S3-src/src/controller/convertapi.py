from os import getenv
from dotenv import load_dotenv

class ConvertApi:
    
    def __init__(self):
        load_dotenv()
        self.API_KEY = getenv('API_KEY_PDF')
    
    def extraer_imagenes(self, files):
        pass
    
    def unir_pdfs(self, files):
        pass
    
    def convertir_archivo(self, files, convert_to):
        pass
    
    