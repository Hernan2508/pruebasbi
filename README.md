# 📄 Configuración de Variables de Entorno

Este proyecto utiliza archivos `.env` para manejar credenciales, rutas y configuraciones específicas tanto **globales** como **locales por proyecto**.  
Para mantener buenas prácticas, todos los archivos sensibles están excluidos del repositorio utilizando `.gitignore`.

--Sigue los pasos a continuación para preparar tu entorno correctamente.

---

## 🧩 1. Variables globales (archivo principal)

El archivo **`.env.example`** contiene la estructura base con todas las variables generales del sistema.

### Pasos:

1. Copiar el archivo de ejemplo:
   ```bash
   cp .env.example .env

2. Abrir el archivo .env y completar los valores:
URL_API=http://localhost:8000
DATABASE_URL=postgres://user:pass@localhost:5432/db
TOKEN_SECRET=xxxxxx


⚠️ Importante: Nunca subas el archivo .env al repositorio. Solo .env.example debe estar versionado.

2. Variables locales por proyecto

Cada proyecto interno requiere configuraciones adicionales, como rutas locales, directorios de entrada/salida, parámetros específicos o credenciales de origen de datos.

Por ello, se incluyen archivos:

proyecto01.env.example
proyecto02.env.example
proyecto03.env.example
(y así sucesivamente según tus módulos)

Estos archivos contienen la plantilla de variables requeridas para cada proyecto.

Pasos para cada proyecto:
👉 Proyecto 01

Copiar el archivo:

cp proyecto01.env.example proyecto01.env


Editar proyecto01.env con tus valores locales:

INPUT_DIR=C:/proyecto01/inputs
OUTPUT_DIR=C:/proyecto01/outputs
FECHA_INICIO=2025-01-01
FECHA_FIN=2025-01-31

👉 Proyecto 02

Copiar:

cp proyecto02.env.example proyecto02.env


Configurar valores locales:

RUTA_ORIGEN=D:/data/source
RUTA_DESTINO=D:/data/output
LOG_LEVEL=INFO


(Repetir el mismo patrón para los demás proyectos)

✔️ 3. ¿Por qué este esquema?

Permite centralizar variables generales del entorno en .env.

Mantiene aisladas las configuraciones específicas de cada proyecto.

Evita exponer credenciales, rutas y configuraciones locales en GitHub.

Facilita la colaboración entre equipos: cada desarrollador solo rellena sus .env reales en su máquina.

Cumple buenas prácticas DevOps y evita conflictos en despliegues.

🚀 4. Carga automática en el proyecto

El código del proyecto debe usar la librería correspondiente para cargar:

.env → variables globales

proyectoXX.env → variables específicas del módulo que ejecutes

Ejemplo en Python:

from dotenv import load_dotenv
import os

load_dotenv(".env")               # Variables globales
load_dotenv("proyecto01.env")     # Variables locales del proyecto actual

print(os.getenv("INPUT_DIR"))
print(os.getenv("DATABASE_URL"))

🛑 Buenas prácticas recomendadas

Nunca subas .env reales al repositorio.

Mantén siempre actualizados los .env.example para indicar qué variables se requieren.

Evita duplicar variables entre los .env locales y el global.

Documenta valores por defecto cuando sea posible.

❓ ¿Necesitas añadir más proyectos?

Puedo generar automáticamente:

proyecto03.env.example

proyecto04.env.example

…

Solo indícame cuántos módulos o proyectos deseas documentar.