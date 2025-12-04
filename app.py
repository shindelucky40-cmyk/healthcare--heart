import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ----------------------------- PAGE CONFIG -----------------------------
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

# Load model & scaler
model = joblib.load("heart_rf_model.pkl")
scaler = joblib.load("scaler.pkl")

# ----------------------------- STYLING -----------------------------
st.markdown("""
<style>
    .main {
        background-color: #fafafa;
    }
    .stTitle {
        text-align: center;
    }
    .prediction-card {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 22px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------- SIDEBAR -----------------------------
st.sidebar.title("⚙️ Navigation")
st.sidebar.info("Fill in the details on the right to predict heart disease risk.")

st.sidebar.markdown("### 📌 About")
st.sidebar.write("A machine learning app using Random Forest to predict heart disease risk.")

# ----------------------------- MAIN TITLE -----------------------------
st.title("❤️ Heart Disease Prediction App")
st.caption("Enter patient details below to check the risk.")

st.write("---")

# ----------------------------- INPUT SECTIONS -----------------------------
st.subheader("🧑‍⚕️ Patient Medical Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 20, 100, 45)
    sex = st.selectbox("Sex", ["Female (0)", "Male (1)"])
    sex = 0 if sex == "Female (0)" else 1

    trestbps = st.number_input("Resting Blood Pressure (trestbps)", 80, 200, 120)
    chol = st.number_input("Cholesterol (chol)", 100, 600, 200)

with col2:
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
    thalach = st.number_input("Max Heart Rate (thalach)", 60, 250, 150)
    exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
    oldpeak = st.number_input("Oldpeak (ST Depression)", 0.0, 10.0, 1.0)

st.write("---")
st.subheader("🧬 Encoded Medical Categories")

# ================= CHEST PAIN =================
cp = st.selectbox("Chest Pain Type (cp)", ["cp_1", "cp_2", "cp_3", "cp_4"])
cp_1 = 1 if cp == "cp_1" else 0
cp_2 = 1 if cp == "cp_2" else 0
cp_3 = 1 if cp == "cp_3" else 0
cp_4 = 1 if cp == "cp_4" else 0

# ================= SLOPE =================
slope = st.selectbox("Slope", ["slope_1", "slope_2", "slope_3"])
slope_1 = 1 if slope == "slope_1" else 0
slope_2 = 1 if slope == "slope_2" else 0
slope_3 = 1 if slope == "slope_3" else 0

# ================= CA =================
ca = st.selectbox("CA", ["ca_1","ca_2","ca_3","ca_4"])
ca_1 = 1 if ca == "ca_1" else 0
ca_2 = 1 if ca == "ca_2" else 0
ca_3 = 1 if ca == "ca_3" else 0
ca_4 = 1 if ca == "ca_4" else 0

# ================= THAL =================
thal = st.selectbox("Thal", ["thal_1","thal_2","thal_3"])
thal_1 = 1 if thal == "thal_1" else 0
thal_2 = 1 if thal == "thal_2" else 0
thal_3 = 1 if thal == "thal_3" else 0

# ================= AGE BIN =================
age_bin = st.selectbox("Age Group", ["35-50", "50-65", "65+"])
age_bin_35_50 = 1 if age_bin == "35-50" else 0
age_bin_50_65 = 1 if age_bin == "50-65" else 0
age_bin_65_plus = 1 if age_bin == "65+" else 0

st.write("---")

# ----------------------------- BUILD INPUT DATA -----------------------------
input_data = pd.DataFrame([{
    "age": age,
    "sex": sex,
    "trestbps": trestbps,
    "chol": chol,
    "fbs": fbs,
    "thalach": thalach,
    "exang": exang,
    "oldpeak": oldpeak,
    "cp_1": cp_1, "cp_2": cp_2, "cp_3": cp_3, "cp_4": cp_4,
    "slope_1": slope_1, "slope_2": slope_2, "slope_3": slope_3,
    "ca_1": ca_1, "ca_2": ca_2, "ca_3": ca_3, "ca_4": ca_4,
    "thal_1": thal_1, "thal_2": thal_2, "thal_3": thal_3,
    "age_bin_35-50": age_bin_35_50,
    "age_bin_50-65": age_bin_50_65,
    "age_bin_65+": age_bin_65_plus
}])

scaled_input = scaler.transform(input_data)

# ----------------------------- PREDICTION -----------------------------
if st.button("🔍 Predict"):
    pred = model.predict(scaled_input)[0]

    if pred == 1:
        st.markdown(
            "<div class='prediction-card' style='background-color:#ffe6e6; color:#b30000;'>"
            "⚠️ High Chance of Heart Disease"
            "</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div class='prediction-card' style='background-color:#e6ffe6; color:#006600;'>"
            "✔️ Low Chance of Heart Disease"
            "</div>",
            unsafe_allow_html=True
        )
