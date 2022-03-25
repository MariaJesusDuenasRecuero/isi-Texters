from os import getenv
from dotenv import load_dotenv

class MeaningCloud:
    
    def __init__(self):
        load_dotenv()
        self.API_KEY = getenv('API_KEY_RESUMEN')
        
    
    def resumir(self, files):
        pass