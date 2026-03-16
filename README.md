# Cybersecurity Analytics Project (2015-2024)

Proyecto de análisis de datos sobre amenazas de ciberseguridad entre 2015 y 2024.

Tecnologías utilizadas:
- Python
- Pandas
- MySQL
- Streamlit

## Dataset

Global Cybersecurity Threats (2015-2024)

## Estructura del proyecto

cybersecurity-analytics-project

data/
dataset utilizado

database/
scripts SQL

analysis/
analisis de datos

app/
dashboard en Streamlit

landing/
landing page del proyecto

## Consultas SQL

1 Ataques por año

SELECT year, COUNT(*) 
FROM cyber_attacks
GROUP BY year;

2 Industrias más atacadas

SELECT target_industry, COUNT(*) 
FROM cyber_attacks
GROUP BY target_industry;

3 Países con más ataques

SELECT country, COUNT(*) 
FROM cyber_attacks
GROUP BY country
ORDER BY COUNT(*) DESC;

## Dashboard

Para ejecutar el dashboard:

streamlit run app/app.py

## Integrante

Jaduer

## Repositorio

https://github.com/Genuino07/cybersecurity-analytics-project
