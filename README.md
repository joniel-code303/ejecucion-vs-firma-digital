# ejecucion-vs-firma-digital
Demostración de la diferencia entre ejecutar código sin verificación y con firma digital usando HMAC-SHA256. Este script resalta la importancia de validar la integridad del código antes de su ejecución para prevenir modificaciones maliciosas.



# Clonar el repositorio
git clone https://github.com/tu-usuario/ejecucion-vs-firma-digital.git
cd ejecucion-vs-firma-digital


# Instalar dependencias
pip install -r requirements.txt


# Ejecutar demostración principal
python ejecucion_firma_digital.py


# Ejecutar firma y verificación de nuevo código
python -c "
from ejecucion_firma_digital import generar_firma_digital, ejecutar_codigo_con_firma


codigo = 'print(\"Hola\")'
firma = generar_firma_digital(codigo)
print(f'Firma generada: {firma}')
ejecutar_codigo_con_firma(codigo, firma)
"


# Ejecutar pruebas
python -m unittest discover tests














firma-digital-ejecucion/
├── src/
│   ├── ejecucion_firma_digital.py  # Script principal
│   └── utils.py                    # Funciones auxiliares (extendido)
├── tests/
│   ├── test_firma_digital.py       # Pruebas unitarias
│   └── test_ejecucion.py           # Pruebas de ejecución
├── examples/
│   ├── codigo_seguro.py            # Ejemplo de código firmado
│   └── codigo_alterado.py          # Ejemplo de código modificado
├── docs/
│   ├── explicacion.md              # Explicación técnica
│   └── uso.md                      # Guía de uso
├── requirements.txt                # Dependencias
├── LICENSE                         # Licencia MIT
└── README.md                       # Este archivo












