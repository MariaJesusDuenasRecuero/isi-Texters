from os import getenv
import os
from unittest import result
from dotenv import load_dotenv
import convertapi

class ConvertApi:
    
    def __init__(self):
        load_dotenv()
        self.API_KEY = getenv('API_KEY_PDF')
        convertapi.api_secret=self.API_KEY
    
    def extraer_imagenes(self, files): # supongo es un unico archivo
        if methods.comprobar_extension('.pdf',files):
            return convertapi.convert('extract-images', {'File': files}, from_format='pfd')
        return None
        
    
    def unir_pdfs(self, files): #supongo que files es un array
        if len(files)>=2 & methods.comprobar_extensiones('.pdf',files):
            return convertapi.convert('merge',{'Files': files}, from_format='pfd')
        return None

    def convertir_archivo(self, files, convert_to): #supongo es un unico archivo
        if convert_to.lower()=='pdf' & methods.comprobar_extension('.word',files):
            return convertapi.convert(convert_to, {'File': files})   
        elif methods.comprobar_extensiones('.pdf',files):
            return convertapi.convert(convert_to, {'File': files})
        return None

class methods:
    def comprobar_extensiones(extension_type, files):

        for file in files:
            name, extension = os.path.splitext(file)
            if extension!=extension_type:
                return False
        return True
        
    def comprobar_extension(extension_type, files):
        name, extension = os.path.splitext(files)
        if extension!=extension_type:
            return False
        return True
