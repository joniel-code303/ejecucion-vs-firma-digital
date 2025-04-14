#!/usr/bin/env python3
"""
Script de demostración: Ejecución tradicional vs Firma Digital

Este script muestra la diferencia entre ejecutar un código sin verificación
y ejecutarlo después de validar su firma digital.
"""

import hashlib
import hmac
import json
from datetime import datetime

# Simulación de una clave secreta compartida (en un caso real, esto estaría seguro)
SECRET_KEY = b'mi_clave_secreta_super_segura_123'

def generar_firma_digital(datos):
    """Genera una firma digital HMAC-SHA256 de los datos"""
    if isinstance(datos, str):
        datos = datos.encode('utf-8')
    elif isinstance(datos, dict):
        datos = json.dumps(datos).encode('utf-8')
    
    return hmac.new(SECRET_KEY, datos, hashlib.sha256).hexdigest()

def ejecutar_codigo_sin_verificacion(codigo):
    """Ejecuta código sin verificación (riesgoso)"""
    print("\n[Ejecución tradicional sin verificación]")
    print("Advertencia: Este método es vulnerable a modificaciones no autorizadas")
    try:
        exec(codigo)
    except Exception as e:
        print(f"Error al ejecutar: {e}")

def ejecutar_codigo_con_firma(codigo, firma):
    """Ejecuta código solo si la firma es válida"""
    print("\n[Ejecución con verificación de firma digital]")
    
    # Verificar la firma
    firma_calculada = generar_firma_digital(codigo)
    
    if not hmac.compare_digest(firma, firma_calculada):
        print("¡Error! Firma digital no válida. El código podría haber sido alterado.")
        return
    
    print("Firma digital verificada. Ejecutando código seguro...")
    try:
        exec(codigo)
    except Exception as e:
        print(f"Error al ejecutar: {e}")

def demostracion():
    # Código de ejemplo que queremos ejecutar
    codigo_seguro = """
def saludo_seguro():
    print("¡Hola desde código firmado digitalmente!")
    print(f"Fecha actual: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

saludo_seguro()
"""
    
    # Generar firma digital del código seguro
    firma_valida = generar_firma_digital(codigo_seguro)
    
    # 1. Demostración de ejecución sin verificación
    print("="*70)
    print("DEMOSTRACIÓN DE EJECUCIÓN TRADICIONAL VS FIRMA DIGITAL")
    print("="*70)
    
    # Ejecutar sin verificación (podría ser código modificado)
    ejecutar_codigo_sin_verificacion(codigo_seguro)
    
    # 2. Demostración de ejecución con verificación de firma
    # Caso correcto
    ejecutar_codigo_con_firma(codigo_seguro, firma_valida)
    
    # Caso con código alterado
    codigo_alterado = codigo_seguro + "\nprint('¡Código malicioso ejecutado!')"
    ejecutar_codigo_con_firma(codigo_alterado, firma_valida)
    
    print("\n" + "="*70)
    print("Conclusiones:")
    print("- La ejecución tradicional no detecta modificaciones en el código")
    print("- La firma digital garantiza la integridad del código antes de ejecutarlo")
    print("- Cualquier modificación invalida la firma y previene la ejecución")

if __name__ == "__main__":
    demostracion()
