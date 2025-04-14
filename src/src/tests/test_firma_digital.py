import unittest
from src.ejecucion_firma_digital import generar_firma_digital
from src.utils import generar_hash, verificar_integridad

class TestFirmaDigital(unittest.TestCase):
    def test_generar_firma(self):
        texto = "Hola mundo"
        firma1 = generar_firma_digital(texto)
        firma2 = generar_firma_digital(texto)
        self.assertEqual(firma1, firma2)
        
        texto_diferente = "Adiós mundo"
        firma3 = generar_firma_digital(texto_diferente)
        self.assertNotEqual(firma1, firma3)
    
    def test_utils_hash(self):
        texto = "Texto de prueba"
        hash1 = generar_hash(texto)
        hash2 = generar_hash(texto)
        self.assertEqual(hash1, hash2)
        self.assertTrue(verificar_integridad(texto, hash1))

if __name__ == '__main__':
    unittest.main()
