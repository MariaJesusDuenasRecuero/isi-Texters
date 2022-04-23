from os import getenv

from injector import T
from dotenv import load_dotenv
import requests
class MeaningCloud:
    
    def __init__(self):
        load_dotenv()
        self.API_KEY = getenv('API_KEY_RESUMIR')
        self.URL = "https://api.meaningcloud.com/summarization-1.0"
        self.confirm = False
        
    def resumir(self, files):
        payload={
            'key' : self.API_KEY,
            'sentences' : '5'
            }
        try:
            response = requests.post(self.URL, files={'doc': open (files,'rb')}, data=payload)
            self.confirm = True
            content = response.json()
            return content
        except:
            print("Algo fue mal.")
            exit()
        
        
        
        