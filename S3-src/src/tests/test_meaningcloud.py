import unittest
import sys,os
p = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(p)
from controller.meaningcloud import * 

CONVERTIR = os.path.join(os.path.dirname(__file__), "/archivos_prueba/convertir.docx")
class TestMeaningcloud(unittest.TestCase):
    
    def test_resumir(self):
        api = MeaningCloud()
        llamada= api.resumir(CONVERTIR)
        self.assertEqual(api.confirm,True)
        self.assertGreater(len(llamada),0)
if __name__ == '__main__':
    unittest.main()