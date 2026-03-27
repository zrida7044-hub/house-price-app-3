import streamlit as st
import joblib
import numpy as np

model = joblib.load("house_model.pkl")

st.title("🏠 House Price Prediction App")

area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")

if st.button("Predict Price"):
    input_data = np.array([[area, bedrooms, bathrooms]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Price: {prediction[0]:,.2f}")