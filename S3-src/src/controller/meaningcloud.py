from os import getenv
from dotenv import load_dotenv
import requests

class MeaningCloud:
    
    def __init__(self):
        load_dotenv()
        self.API_KEY = getenv('API_KEY_RESUMEN')
        self.URL = "https://api.meaningcloud.com/summarization-1.0"
        
    
    def resumir(self, files):
        
        f = open (files,'r')
        mensaje = f.read()
        f.close()
        payload={

            'key' : self.API_KEY,
            'txt' : mensaje,
            'sentences' : '5'
            }

        response = requests.post(self.URL, data=payload)
        response = str(response.json().get("summary"))
        f = open(f'./view/static/downloads/Resumen.txt', 'w')
        f.write(response)
        f.close()
        