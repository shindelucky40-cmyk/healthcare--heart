# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ---------- Load Model ----------
model = joblib.load("heart_rf_model.pkl")

# ---------- Page Config ----------
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.markdown("""
    <h1 style='text-align: center; color: crimson;'>❤️ Heart Disease Prediction ❤️</h1>
    <p style='text-align: center; color: gray;'>Predict your heart disease risk using Random Forest model</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------- Input Form ----------
st.header("Enter your details:")

# Numeric features
age = st.slider("Age", 20, 100, 50)
trestbps = st.slider("Resting Blood Pressure (mm Hg)", 80, 200, 120)
chol = st.slider("Cholesterol (mg/dl)", 100, 400, 200)
thalach = st.slider("Max Heart Rate Achieved", 60, 220, 150)
oldpeak = st.slider("ST Depression (oldpeak)", 0.0, 6.0, 1.0, 0.1)

# Categorical features
sex = st.radio("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
fbs = st.radio("Fasting Blood Sugar > 120 mg/dl?", ["Yes", "No"])
restecg = st.selectbox("Resting ECG Results", ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
exang = st.radio("Exercise Induced Angina?", ["Yes", "No"])
slope = st.selectbox("Slope of ST Segment", ["Upsloping", "Flat", "Downsloping"])
ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", [0,1,2,3,4])
thal = st.selectbox("Thalassemia Type", ["Normal", "Fixed Defect", "Reversible Defect", "Unknown"])

# ---------- Process inputs ----------
# Map to numeric like training
input_data = pd.DataFrame({
    "age": [age],
    "trestbps": [trestbps],
    "chol": [chol],
    "thalach": [thalach],
    "oldpeak": [oldpeak],
    "sex_1": [1 if sex=="Male" else 0],
    "cp_1": [1 if cp=="Atypical Angina" else 0],
    "cp_2": [1 if cp=="Non-Anginal Pain" else 0],
    "cp_3": [1 if cp=="Asymptomatic" else 0],
    "fbs_1": [1 if fbs=="Yes" else 0],
    "restecg_1": [1 if restecg=="ST-T Wave Abnormality" else 0],
    "restecg_2": [1 if restecg=="Left Ventricular Hypertrophy" else 0],
    "exang_1": [1 if exang=="Yes" else 0],
    "slope_1": [1 if slope=="Flat" else 0],
    "slope_2": [1 if slope=="Downsloping" else 0],
    "ca_1": [1 if ca==1 else 0],
    "ca_2": [1 if ca==2 else 0],
    "ca_3": [1 if ca==3 else 0],
    "ca_4": [1 if ca==4 else 0],
    "thal_1": [1 if thal=="Fixed Defect" else 0],
    "thal_2": [1 if thal=="Reversible Defect" else 0],
    "thal_3": [1 if thal=="Unknown" else 0],
})

st.markdown("---")

# ---------- Prediction ----------
if st.button("Predict Heart Disease Risk"):
    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0][prediction]
    
    if prediction == 1:
        st.error(f"⚠️ High risk of heart disease! (Confidence: {prediction_proba:.2f})")
    else:
        st.success(f"✅ Low risk of heart disease. (Confidence: {prediction_proba:.2f})")
