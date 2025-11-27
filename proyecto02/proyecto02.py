# proyecto01/proyecto01.py

import os
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    raise SystemExit(
        "Instala python-dotenv primero: pip install python-dotenv"
    )

# Ruta del archivo .env que está junto al script
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

nombre = os.getenv("NOMBRE", "sin_nombre")

print(f"Hola {nombre} desde proyecto02")