from os import getenv
import os
from select import select
from tkinter import TRUE
from unittest import result

from injector import T
from dotenv import load_dotenv
import convertapi

class ConvertApi:
    
    def __init__(self):
        self.confirm = False;

    def __init__(self):
        load_dotenv()
        self.API_KEY = getenv('API_KEY_PDF')
        convertapi.api_secret=self.API_KEY
    
    def extraer_imagenes(self, files): # supongo es un unico archivo
        try:
            llamada = convertapi.convert('extract-images', {'File': files})
            self.confirm = True
            return llamada
        except:
            print("Algo salió mal.")
    def unir_pdfs(self, files): #supongo que files es un array
        try:
            llamada = convertapi.convert('merge',{'Files': files}, from_format='pdf')
            self.confirm = True
            return llamada
        except:
            print("Algo salió mal.")

    def convertir_archivo(self, files, convert_to): #supongo es un unico archivo
        try:
            llamada = convertapi.convert(convert_to, {'File': files})  
            self.confirm = True
            return llamada  
        except:
            print("Algo salió mal.")

