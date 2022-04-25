from os import getenv
from dotenv import load_dotenv
import requests

class MeaningCloud:
    
    def __init__(self):
        load_dotenv()
        self.API_KEY = getenv('API_KEY_RESUMIR')
        self.URL = "https://api.meaningcloud.com/summarization-1.0"
        
    def resumir(self, files, sentences):
        payload={
            'key' : self.API_KEY,
            'sentences' : sentences
            }
        response = requests.post(self.URL, files={'doc': open (files,'rb')}, data=payload)
        content = response.json()
        
        return content
        