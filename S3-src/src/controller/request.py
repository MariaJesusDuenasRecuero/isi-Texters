from enum import Enum
from lib2to3.pytree import convert

from controller.convertapi import ConvertApi
from controller.meaningcloud import MeaningCloud

class Request:
    
    def __init__(self, request, files, convert_to = None) -> None:
        self.request = request
        self.files = files
        self.convert_to = convert_to
    
    def realizar_peticion(self):
        if self.request==requests.CONVERTIR:
            return ConvertApi.convertir_archivo(self.files, self.convert_to)
        elif self.request==requests.ESCANEAR:
            return ConvertApi.extraer_imagenes(self.files)
        elif self.request==requests.UNIR:
            return ConvertApi.unir_pdfs(self.files)
        elif self.request==requests.RESUMIR:
            return MeaningCloud.resumir(self.files)
        else:
            return None


class requests(Enum): 
    
    CONVERTIR = 1
    ESCANEAR = 2
    UNIR = 3
    RESUMIR = 4