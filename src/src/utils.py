"""
Funciones auxiliares para el sistema de firma digital
"""

import hashlib
import hmac
import json

def generar_hash(datos, algoritmo='sha256'):
    """Genera un hash de los datos usando el algoritmo especificado"""
    if isinstance(datos, str):
        datos = datos.encode('utf-8')
    elif isinstance(datos, dict):
        datos = json.dumps(datos).encode('utf-8')
    
    hasher = hashlib.new(algoritmo)
    hasher.update(datos)
    return hasher.hexdigest()

def verificar_integridad(datos, hash_esperado, algoritmo='sha256'):
    """Verifica que los datos coincidan con el hash esperado"""
    return generar_hash(datos, algoritmo) == hash_esperado
