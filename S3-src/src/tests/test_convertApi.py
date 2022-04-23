from inspect import CO_ASYNC_GENERATOR
import unittest
import sys,os
p = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(p)
from controller.convertapi import * 

IMAGENES = os.path.join(os.path.dirname(__file__), "/archivos_prueba/extraerImagenes.pdf")
CONVERTIR = os.path.join(os.path.dirname(__file__), "/archivos_prueba/convertir.docx")
MERGE1 =  os.path.join(os.path.dirname(__file__), "/archivos_prueba/file1.docx")
MERGE2 =  os.path.join(os.path.dirname(__file__), "/archivos_prueba/file2.docx")
MERGE = [MERGE1, MERGE2]

class TestConvertApi(unittest.TestCase):
    

    def test_images(self):
        api = ConvertApi()
        llamada= api.extraer_imagenes(IMAGENES)
        self.assertEqual(api.confirm,True)
    
    def test_summary(self):
        api = ConvertApi()
        llamada= api.convertir_archivo(CONVERTIR, "pdf")
        self.assertEqual(api.confirm,True)

    def test_merge(self):
        api = ConvertApi()
        llamada= api.unir_pdfs(MERGE)
        self.assertEqual(api.confirm,True)

if __name__ == '__main__':
    unittest.main()