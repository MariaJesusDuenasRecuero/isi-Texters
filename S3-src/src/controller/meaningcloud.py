from os import getenv
from dotenv import load_dotenv
import requests

class MeaningCloud:
    
    def __init__(self):
        load_dotenv()
        self.API_KEY = getenv('API_KEY_RESUMEN')
        self.URL = "https://api.meaningcloud.com/summarization-1.0"
        
    
    def resumir(self, files):
        payload={

            'key' : self.API_KEY,
            'txt' : files,
            'sentences' : '5'
            }

        response = requests.post(self.URL, data=payload)
        return response.json()