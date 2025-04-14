# Explicación Técnica

## Firma Digital para Ejecución de Código

Este sistema demuestra cómo usar firmas digitales para garantizar la integridad del código antes de su ejecución.

### Componentes clave:

1. **HMAC-SHA256**: Algoritmo usado para generar la firma
2. **Clave secreta**: Solo conocida por el emisor y verificador
3. **Comparación segura**: Usa `hmac.compare_digest` para prevenir ataques de timing

### Flujo de trabajo:

1. El desarrollador genera el código y su firma
2. Distribuye ambos (código + firma)
3. Antes de ejecutar, el sistema verifica la firma
4. Solo ejecuta si la verificación es exitosa
