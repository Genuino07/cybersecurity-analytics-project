import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("Cybersecurity Threat Analysis (2015-2024)")

# ruta segura del dataset
data_path = os.path.join("data", "cybersecurity.csv")

# cargar datos
df = pd.read_csv(data_path)

st.subheader("Dataset Preview")
st.dataframe(df.head())

# ataques por año
st.subheader("Cyber Attacks by Year")

attacks_year = df.groupby("year").size().reset_index(name="attacks")

fig1 = px.line(
    attacks_year,
    x="year",
    y="attacks",
    markers=True,
    title="Cyber Attacks per Year"
)

st.plotly_chart(fig1)

# ataques por industria
st.subheader("Most Targeted Industries")

industry = df["target_industry"].value_counts().reset_index()
industry.columns = ["industry", "attacks"]

fig2 = px.bar(
    industry,
    x="industry",
    y="attacks",
    title="Attacks by Industry"
)

st.plotly_chart(fig2)

# países más atacados
st.subheader("Top Countries Targeted")

countries = df["country"].value_counts().reset_index()
countries.columns = ["country", "attacks"]

fig3 = px.bar(
    countries.head(10),
    x="country",
    y="attacks",
    title="Top 10 Countries Attacked"
)

st.plotly_chart(fig3)

# pérdidas económicas
st.subheader("Financial Loss by Attack Type")

loss = df.groupby("attack_type")["financial_loss"].sum().reset_index()

fig4 = px.pie(
    loss,
    values="financial_loss",
    names="attack_type",
    title="Financial Loss Distribution"
)

st.plotly_chart(fig4)
