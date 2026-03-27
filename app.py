
import streamlit as st
import joblib
import numpy as np
import os

model_path = os.path.join(os.path.dirname(__file__), "house_model.pkl")
model = joblib.load(model_path)

st.title("🏠 House Price Prediction App")

area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
stories = st.number_input("Stories")
parking = st.number_input("Parking")

mainroad = st.selectbox("Main Road", ["no", "yes"])
guestroom = st.selectbox("Guest Room", ["no", "yes"])
basement = st.selectbox("Basement", ["no", "yes"])
airconditioning = st.selectbox("Air Conditioning", ["no", "yes"])

if st.button("Predict Price"):
    input_data = np.array([[
        area,
        bedrooms,
        bathrooms,
        stories,
        parking,
        1 if mainroad == "yes" else 0,
        1 if guestroom == "yes" else 0,
        1 if basement == "yes" else 0,
        1 if airconditioning == "yes" else 0
    ]])

    prediction = model.predict(input_data)
    st.success(f"Predicted Price: {prediction[0]:,.2f}")