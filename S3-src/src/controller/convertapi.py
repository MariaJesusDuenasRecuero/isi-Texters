from distutils import extension
from os import getenv
import os
from re import T
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
            result= convertapi.convert('extract-images', {'File': files}, from_format='pfd')
            #pensar cómo descargará las images el usuario
        
    
    def unir_pdfs(self, files): #supongo que files es un array
        if len(files)>=2 & methods.comprobar_extensiones('.pdf',files):
            result = convertapi.convert('merge',{'Files': files}, from_format='pfd')
            #pensar cómo descargará el archivo el usuario
    
    def convertir_archivo(self, files, convert_to): #supongo es un unico archivo
        if methods.comprobar_extension(files):
            result = convertapi.convert(convert_to, {'File': files})   
        #hacer que dependiendo del convert_to se compruebe una extensión u otra   

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