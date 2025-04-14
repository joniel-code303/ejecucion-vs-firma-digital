"""
Ejemplo de código seguro que puede ser firmado
"""

from datetime import datetime

def main():
    print("¡Este es un código seguro!")
    print(f"Ejecutado el: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
