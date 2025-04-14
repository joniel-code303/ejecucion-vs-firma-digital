"""
Ejemplo de código alterado (no seguro)
"""

from datetime import datetime
import os

def main():
    print("¡Este código ha sido modificado!")
    print(f"Ejecutado el: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("¡Podría hacer algo malicioso!")
    # os.system("rm -rf /")  # Esto sería catastrófico si se ejecutara

if __name__ == "__main__":
    main()
