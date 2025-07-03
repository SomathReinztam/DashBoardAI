"""
streamlit run dashBoard.py
 
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# Carga el DataFrame 'df'
df = pd.read_csv('iris.csv', sep=',')

# Título de la aplicación
st.title("Análisis del DataFrame 'df'")

# Estructura del DataFrame
st.header("Estructura del DataFrame")
st.write(f"El DataFrame 'df' tiene {df.shape[0]} filas y {df.shape[1]} columnas, todas de tipo float64.")
st.write("Las columnas son: 'sepal length (cm)', 'sepal width (cm)', 'petal length (cm)' y 'petal width (cm)'.")

# Análisis Descriptivo
st.header("Análisis Descriptivo")
st.subheader("Resumen Estadístico")
st.write(df.describe())

# Visualizaciones
st.header("Visualizaciones")
tabs = st.tabs(["Histograma de Longitudes de Sépalos", "Gráfico de Dispersión de Longitudes y Anchuras de Pétalos"])

with tabs[0]:
    st.subheader("Histograma de Distribución de Longitudes de Sépalos")
    fig = px.histogram(df, x="sepal length (cm)", title="Distribución de Longitudes de Sépalos")
    st.plotly_chart(fig, use_container_width=True)

with tabs[1]:
    st.subheader("Gráfico de Dispersión de Longitudes y Anchuras de Pétalos")
    fig = px.scatter(df, x="petal length (cm)", y="petal width (cm)", title="Relación entre Longitudes y Anchuras de Pétalos")
    st.plotly_chart(fig, use_container_width=True)