# Cybersecurity Threats Analysis (2015–2024)

Proyecto de análisis de datos sobre ciberataques globales entre 2015 y 2024 utilizando Python, SQL y visualización de datos.

## Objetivo del Proyecto

Analizar tendencias globales de ciberataques para identificar:

- Países más afectados
- Tipos de ataques más comunes
- Industrias más vulnerables
- Impacto económico de los ataques

Este proyecto integra análisis de datos, modelado de base de datos y visualización interactiva.

---

# Dataset

El proyecto utiliza el dataset:

**Global Cybersecurity Threats (2015-2024)**

Fuente: Kaggle

Contiene información sobre:

- País afectado
- Industria
- Tipo de ataque
- Año
- Pérdidas financieras
- Usuarios afectados
- Tiempo de resolución

---

# Tecnologías utilizadas

- Python
- Pandas
- SQL
- MySQL
- Streamlit
- GitHub

---

# Estructura del Proyecto

cybersecurity-analytics-project

data/
cybersecurity.csv

database/
schema.sql
queries.sql

analysis/
analysis.py

app/
app.py

landing/
index.html

mer/
mer.png

requirements.txt
README.md


---

# Modelo Entidad Relación (MER)

El modelo de base de datos incluye las siguientes entidades:

- Country
- Industry
- Attack Type
- Incidents

Relaciones:

- Un país puede tener múltiples incidentes
- Una industria puede tener múltiples incidentes
- Un tipo de ataque puede ocurrir en múltiples incidentes

---

# Consultas SQL

Se realizaron consultas para analizar:

1. Tipos de ataque más frecuentes
2. Países con más incidentes
3. Industrias más atacadas
4. Pérdidas económicas por año
5. Tiempo promedio de resolución de ataques

Archivo:

database/queries.sql


---

# Dashboard

Se desarrolló un dashboard interactivo utilizando **Streamlit** que permite visualizar:

- Ataques por año
- Ataques por tipo
- Pérdidas económicas por industria
- Dataset completo

Para ejecutar el dashboard:

streamlit run app/app.py


---

# Instalación del proyecto

Clonar el repositorio:

git clone LINK_DEL_REPOSITORIO


Entrar al proyecto:

cd cybersecurity-analytics-project


Crear entorno virtual:

python -m venv .venv


Activar entorno virtual:

Windows

.venv\Scripts\activate


Instalar dependencias:

pip install -r requirements.txt


Ejecutar aplicación:

streamlit run app/app.py


---

# Autor

Proyecto académico de análisis de datos enfocado en ciberseguridad.


