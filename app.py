# app.py
# Phase 4 - Streamlit Web Application
# Run with: python -m streamlit run app.py

import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load("electricity_model.pkl")

# App title and description
st.title("Electricity Consumption Prediction")
st.write("Predict Power Consumption in Zone 1 using environmental conditions.")
st.markdown("---")

# Input fields
st.subheader("Enter Environmental Conditions")

temperature = st.number_input(
    "Temperature (C)",
    min_value=3.0,
    max_value=40.0,
    value=18.0,
    step=0.1
)

humidity = st.number_input(
    "Humidity (%)",
    min_value=11.0,
    max_value=95.0,
    value=68.0,
    step=0.1
)

wind_speed = st.number_input(
    "Wind Speed",
    min_value=0.0,
    max_value=7.0,
    value=2.0,
    step=0.01
)

general_diffuse_flows = st.number_input(
    "General Diffuse Flows",
    min_value=0.0,
    max_value=1200.0,
    value=183.0,
    step=0.1
)

diffuse_flows = st.number_input(
    "Diffuse Flows",
    min_value=0.0,
    max_value=940.0,
    value=75.0,
    step=0.1
)

st.markdown("---")

# Predict button
if st.button("Predict Consumption"):

    # Create a DataFrame with the user's input values
    input_data = pd.DataFrame(
        [[temperature, humidity, wind_speed, general_diffuse_flows, diffuse_flows]],
        columns=["Temperature", "Humidity", "WindSpeed",
                 "GeneralDiffuseFlows", "DiffuseFlows"]
    )

    # Make prediction using the loaded model
    prediction = model.predict(input_data)

    # Display the result
    st.success(f"Predicted Zone 1 Power Consumption:  {round(prediction[0], 2)} watts")
