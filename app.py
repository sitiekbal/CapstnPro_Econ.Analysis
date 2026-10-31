import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load saved model with resource caching
@st.cache_resource
def load_model():
    return joblib.load('trend_model.pkl')

model = load_model()

# Header
st.title("🌱 Renewable Energy Trend Forecaster")
st.write("Linear Regression model predicting renewable energy generation over time.")

# User Input Widget for Time / Year
year_input = st.number_input("Enter Year (or Time Index):", value=2025, step=1)

# Forecast Button
if st.button("Forecast"):
    # 1. Prepare input array matching the shape expected by trend_model
    # If X_time was fit on a DataFrame column or 2D array:
    input_data = np.array([[year_input]])
    
    # 2. Make forecast
    forecast = model.forecast(input_data)
    
    # 3. Display result
    st.success(f"Forecast Renewable Energy Output: **{forecast:,.2f}**")
