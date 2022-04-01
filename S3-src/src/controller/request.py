from enum import Enum
import ocrmypdf
import os

from controller.convertapi import ConvertApi
from controller.meaningcloud import MeaningCloud

class Request:
    
    def __init__(self, request, files, convert_to = None):
        self.request = request
        self.files = files
        self.convert_to = convert_to

    def ocr(self, file):
        result_file = os.path.basename(file) + "_OCR.pdf"
        save_path = os.path.join(os.path.dirname(os.path.dirname(__file__)) + '/view/static/downloads/' + result_file)
        ocrmypdf.ocr(file, save_path, deskew=True)
    
    def realizar_peticion(self):
        if self.request==requests.CONVERTIR:
            return ConvertApi().convertir_archivo(files=self.files,convert_to=self.convert_to)
        elif self.request==requests.ESCANEAR:
            return ConvertApi().extraer_imagenes(self.files)
        elif self.request==requests.UNIR:
            return ConvertApi().unir_pdfs(self.files)
        elif self.request==requests.RESUMIR:
            return MeaningCloud().resumir(self.files)
        elif self.request==requests.OCR:
            self.ocr(self.files)
        else:
            return None



class requests(Enum): 
    
    CONVERTIR = 1
    ESCANEAR = 2
    UNIR = 3
    RESUMIR = 4
    OCR = 5