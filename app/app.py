import streamlit as st
import pandas as pd

# título

st.title("Cybersecurity Threats Analysis 2015-2024")

st.write("Dashboard de análisis de ciberataques globales")

# cargar dataset

df = pd.read_csv("data/cybersecurity.csv")

# sidebar filtros

st.sidebar.header("Filtros")

year = st.sidebar.selectbox(
"Año",
sorted(df["year"].unique())
)

industry = st.sidebar.selectbox(
"Industria",
["Todas"] + list(df["industry"].unique())
)

# aplicar filtros

filtered = df[df["year"] == year]

if industry != "Todas":
    filtered = filtered[filtered["industry"] == industry]

# mostrar dataset

st.subheader("Datos filtrados")

st.dataframe(filtered)

# ataques por tipo

st.subheader("Tipos de ataques")

attacks = filtered["attack_type"].value_counts()

st.bar_chart(attacks)

# pérdidas económicas

st.subheader("Pérdidas económicas")

loss = filtered.groupby("industry")["financial_loss"].sum()

st.bar_chart(loss)

# usuarios afectados

st.subheader("Usuarios afectados")

users = filtered.groupby("country")["affected_users"].sum()

st.bar_chart(users)
