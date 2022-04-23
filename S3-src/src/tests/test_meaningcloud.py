import unittest
import sys,os
p = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(p)
from controller.meaningcloud import * 


class TestConvertApi(unittest.TestCase):
    
    def test_resumir(self):
        api = ConvertApi()
        llamada= api.extraer_imagenes()
        self.assertEqual(api.confirm,True)

if __name__ == '__main__':
    unittest.main()