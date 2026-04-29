# 📊 Financial Dashboard API (Español)

---

## 📌 Descripción

API REST que procesa extractos bancarios en CSV, categoriza automáticamente cada transacción por palabras clave y genera un dashboard HTML interactivo con gráficas de torta y barras. Incluye endpoint de resumen en JSON para integración con otros sistemas.

Proyecto desarrollado como parte de un plan de aprendizaje de Python enfocado en desarrollo backend.

**GitHub:** https://github.com/SergioArdCr/financial_dashboard

---

## 🛠️ Tecnologías

| Librería | Uso |
|---|---|
| `FastAPI` | Framework web para construir la API |
| `SQLAlchemy` | ORM para manejo de base de datos |
| `PostgreSQL` | Almacenamiento de transacciones |
| `pandas` | Procesamiento y análisis del CSV |
| `Plotly` | Gráficas interactivas en HTML |
| `Jinja2` | Motor de templates para el reporte HTML |
| `python-multipart` | Soporte para recepción de archivos |

---

## 📁 Estructura

```
W20-Financial-Dashboard/
├── main.py
├── .env
├── .gitignore
├── requirements.txt
├── config/
│   └── settings.py
├── app/
│   ├── db/
│   │   └── database.py
│   ├── models/
│   │   └── transaccion.py
│   ├── schemas/
│   │   └── transaccion.py
│   ├── services/
│   │   ├── categorizer.py
│   │   └── report_generator.py
│   ├── routers/
│   │   └── finanzas.py
│   └── templates/
│       └── reporte.html
└── data/
    └── extracto.csv
```

---

## ⚙️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/SergioArdCr/financial_dashboard.git
cd financial_dashboard

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus valores

# Correr el servidor
uvicorn main:app --reload
```

---

## 🔐 Variables de entorno

```env
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/financial_dashboard
```

---

## 🗃️ Modelo de base de datos

```
transacciones
├── id           — identificador único
├── fecha        — fecha de la transacción
├── descripcion  — descripción del movimiento
├── monto        — valor en pesos (siempre positivo)
└── categoria    — categoría asignada automáticamente
```

---

## 🚀 Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/upload` | Sube un CSV y categoriza las transacciones |
| `GET` | `/reporte` | Devuelve el dashboard HTML con gráficas |
| `GET` | `/resumen` | Devuelve totales por categoría en JSON |

---

## 📄 Formato del CSV

El archivo CSV debe tener exactamente estas tres columnas:

```csv
fecha,descripcion,monto
2026-01-05,Restaurante El Corral,45000
2026-01-07,Uber viaje centro,18000
2026-01-10,Netflix suscripcion,17900
```

| Columna | Tipo | Descripción |
|---|---|---|
| `fecha` | `YYYY-MM-DD` | Fecha de la transacción |
| `descripcion` | texto | Descripción del movimiento |
| `monto` | número | Valor (positivo o negativo, se normaliza) |

---

## 🏷️ Categorías disponibles

| Categoría | Palabras clave detectadas |
|---|---|
| Alimentación | restaurante, supermercado, rappi, exito, carulla... |
| Transporte | uber, taxi, gasolina, peaje, transmilenio... |
| Entretenimiento | netflix, spotify, steam, cine, disney... |
| Salud | farmacia, drogueria, medico, clinica, gym... |
| Servicios | energia, agua, internet, telefono, claro... |
| Educacion | universidad, curso, udemy, libro... |
| Ropa | zara, adidas, nike, falabella... |
| Otros | cualquier descripción no reconocida |

---

## 💡 Ejemplo de uso

```python
import httpx

BASE_URL = "http://localhost:8000"

# 1. Subir extracto bancario
with open("data/extracto.csv", "rb") as f:
    response = httpx.post(f"{BASE_URL}/upload", files={"file": f})
print(response.json())
# {"mensaje": "15 transacciones cargadas correctamente"}

# 2. Ver resumen en JSON
resumen = httpx.get(f"{BASE_URL}/resumen")
print(resumen.json())
# [
#   {"categoria": "Alimentación", "total": 306000.0, "cantidad": 4},
#   {"categoria": "Transporte",   "total": 125000.0, "cantidad": 3},
#   ...
# ]

# 3. Ver dashboard HTML
# Abrir en el navegador: http://localhost:8000/reporte
```

---

## 💡 Aprendizajes clave

- Recepción y procesamiento de archivos con `UploadFile` y `io.BytesIO`
- Categorización automática por palabras clave con diccionario de reglas
- Gráficas interactivas con Plotly — pie chart y bar chart
- Templates HTML dinámicos con Jinja2 — variables, filtros, `| safe`
- Diferencia entre `fig.show()` (standalone) y `fig.to_html()` (embebido en API)
- Agrupación y análisis de datos con `pandas.groupby()`
- Conversión de objetos SQLAlchemy a DataFrame para análisis
- Agregaciones en SQLAlchemy con `func.sum()` y `func.count()`

---
---

# 📊 Financial Dashboard API (English)

---

## 📌 Description

REST API that processes bank statements in CSV format, automatically categorizes each transaction by keyword matching, and generates an interactive HTML dashboard with pie and bar charts. Includes a JSON summary endpoint for integration with other systems.

Built as part of a Python learning plan focused on backend development.

**GitHub:** https://github.com/SergioArdCr/financial_dashboard

---

## 🛠️ Tech Stack

| Library | Usage |
|---|---|
| `FastAPI` | Web framework for building the API |
| `SQLAlchemy` | ORM for database management |
| `PostgreSQL` | Transaction storage |
| `pandas` | CSV processing and analysis |
| `Plotly` | Interactive HTML charts |
| `Jinja2` | Template engine for HTML report |
| `python-multipart` | File upload support |

---

## 📁 Structure

```
W20-Financial-Dashboard/
├── main.py
├── .env
├── .gitignore
├── requirements.txt
├── config/
│   └── settings.py
├── app/
│   ├── db/
│   │   └── database.py
│   ├── models/
│   │   └── transaccion.py
│   ├── schemas/
│   │   └── transaccion.py
│   ├── services/
│   │   ├── categorizer.py
│   │   └── report_generator.py
│   ├── routers/
│   │   └── finanzas.py
│   └── templates/
│       └── reporte.html
└── data/
    └── extracto.csv
```

---

## ⚙️ Setup

```bash
# Clone the repository
git clone https://github.com/SergioArdCr/financial_dashboard.git
cd financial_dashboard

# Create virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your values

# Run the server
uvicorn main:app --reload
```

---

## 🔐 Environment Variables

```env
DATABASE_URL=postgresql://user:password@localhost:5432/financial_dashboard
```

---

## 🗃️ Database Model

```
transacciones
├── id           — unique identifier
├── fecha        — transaction date
├── descripcion  — movement description
├── monto        — amount in COP (always positive)
└── categoria    — automatically assigned category
```

---

## 🚀 Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/upload` | Upload a CSV and categorize transactions |
| `GET` | `/reporte` | Returns interactive HTML dashboard |
| `GET` | `/resumen` | Returns totals per category in JSON |

---

## 📄 CSV Format

The CSV file must have exactly these three columns:

```csv
fecha,descripcion,monto
2026-01-05,Restaurante El Corral,45000
2026-01-07,Uber viaje centro,18000
2026-01-10,Netflix suscripcion,17900
```

| Column | Type | Description |
|---|---|---|
| `fecha` | `YYYY-MM-DD` | Transaction date |
| `descripcion` | text | Movement description |
| `monto` | number | Amount (positive or negative, gets normalized) |

---

## 🏷️ Available Categories

| Category | Detected keywords |
|---|---|
| Alimentación | restaurante, supermercado, rappi, exito, carulla... |
| Transporte | uber, taxi, gasolina, peaje, transmilenio... |
| Entretenimiento | netflix, spotify, steam, cine, disney... |
| Salud | farmacia, drogueria, medico, clinica, gym... |
| Servicios | energia, agua, internet, telefono, claro... |
| Educacion | universidad, curso, udemy, libro... |
| Ropa | zara, adidas, nike, falabella... |
| Otros | any unrecognized description |

---

## 💡 Usage Example

```python
import httpx

BASE_URL = "http://localhost:8000"

# 1. Upload bank statement
with open("data/extracto.csv", "rb") as f:
    response = httpx.post(f"{BASE_URL}/upload", files={"file": f})
print(response.json())
# {"mensaje": "15 transacciones cargadas correctamente"}

# 2. Get JSON summary
summary = httpx.get(f"{BASE_URL}/resumen")
print(summary.json())
# [
#   {"categoria": "Alimentación", "total": 306000.0, "cantidad": 4},
#   {"categoria": "Transporte",   "total": 125000.0, "cantidad": 3},
#   ...
# ]

# 3. View HTML dashboard
# Open in browser: http://localhost:8000/reporte
```

---

## 💡 Key Learnings

- File upload and processing with `UploadFile` and `io.BytesIO`
- Automatic categorization by keyword matching with rules dictionary
- Interactive charts with Plotly — pie chart and bar chart
- Dynamic HTML templates with Jinja2 — variables, filters, `| safe`
- Difference between `fig.show()` (standalone) and `fig.to_html()` (embedded in API)
- Data grouping and analysis with `pandas.groupby()`
- Converting SQLAlchemy objects to DataFrame for analysis
- SQLAlchemy aggregations with `func.sum()` and `func.count()`
