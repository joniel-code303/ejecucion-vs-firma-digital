import unittest
from src.ejecucion_firma_digital import ejecutar_codigo_con_firma, generar_firma_digital

class TestEjecucionSegura(unittest.TestCase):
    def test_ejecucion_valida(self):
        codigo = "print('Hola')"
        firma = generar_firma_digital(codigo)
        # Debe ejecutarse sin errores
        ejecutar_codigo_con_firma(codigo, firma)
    
    def test_ejecucion_invalida(self):
        codigo = "print('Hola')"
        codigo_alterado = "print('Adiós')"
        firma = generar_firma_digital(codigo)
        # No debe ejecutar el código alterado
        ejecutar_codigo_con_firma(codigo_alterado, firma)

if __name__ == '__main__':
    unittest.main()
