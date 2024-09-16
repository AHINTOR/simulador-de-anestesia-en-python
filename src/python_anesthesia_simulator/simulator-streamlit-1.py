import streamlit as st
import numpy as np
import pandas as pd

# Asegúrate de tener importadas las clases necesarias como 'Patient' y modelos

# Título de la aplicación
st.title("Simulación de Anestesia para un Paciente")

# Sección de entrada de datos para las características del paciente
st.header("Características del Paciente")
age = st.number_input("Edad (años)", value=30)
height = st.number_input("Altura (cm)", value=170)
weight = st.number_input("Peso (kg)", value=70)
gender = st.selectbox("Género", options=["Femenino", "Masculino"], index=0)

# Convertir la entrada de género a 0 (femenino) o 1 (masculino)
gender_value = 0 if gender == "Femenino" else 1

# Parámetros adicionales de simulación
st.header("Parámetros de Simulación")
co_base = st.number_input("Gasto Cardíaco Inicial (L/min)", value=6.5)
map_base = st.number_input("Presión Arterial Media Inicial (mmHg)", value=90)

# Inicializar el paciente y ejecutar simulación al presionar el botón
if st.button("Ejecutar Simulación"):
    # Crear instancia del paciente
    patient = Patient(
        patient_characteristic=[age, height, weight, gender_value],
        co_base=co_base,
        map_base=map_base
    )
    
    # Simular un paso (puedes expandir esto con más lógica)
    bis, co, map_value, tol = patient.one_step()

    # Mostrar los resultados de la simulación
    st.subheader("Resultados de la Simulación")
    st.write(f"BIS: {bis}")
    st.write(f"Gasto Cardíaco (CO): {co} L/min")
    st.write(f"Presión Arterial Media (MAP): {map_value} mmHg")
    st.write(f"Tolerancia (TOL): {tol}")

    # Mostrar el dataframe de resultados si hay datos guardados
    if not patient.data.empty:
        st.dataframe(patient.data)
