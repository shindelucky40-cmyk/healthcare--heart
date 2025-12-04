# ❤️ Heart Disease Prediction (Machine Learning)

A machine learning project that predicts whether a person has a high chance of heart disease based on common medical features.  
This project uses data preprocessing, EDA, and a Random Forest model with very high accuracy.

---

## ⭐ Features of This Project
- Cleaned and processed healthcare dataset  
- Data visualization (EDA)  
- Multiple ML models tested  
- Random Forest selected as the best model  
- Saved model + scaler as `.pkl` files  
- Interactive Streamlit web app  
- Ready for deployment on Streamlit Cloud  

---

## 📂 Project Structure

healthcare-heart/
│── processed.ipynb # Data cleaning + preprocessing
│── model_training.ipynb # ML model training + evaluation
│── heart_rf_model.pkl # Final saved Random Forest model
│── scaler.pkl # Scaler for input normalization
│── healthcare_processed.csv # Preprocessed dataset
│── app.py # Streamlit web application
│── requirements.txt # Dependencies
└── README.md # Project documentation


---

## 🧠 ML Models Used

| Model                | Accuracy |
|----------------------|----------|
| Logistic Regression  | ~85%     |
| Random Forest        | ~99%     |

✔ **Random Forest is used as the final model**  
✔ Very high accuracy and stable predictions  

---

## 🔍 What the Project Does
- Loads healthcare heart-disease dataset  
- Cleans the data  
- Encodes & scales features  
- Splits data into training/testing  
- Tests two ML models  
- Saves best model as `.pkl`  
- Builds a Streamlit interface for predictions  

---

## 📊 Exploratory Data Analysis (EDA)
The project includes the following visualizations:

- Correlation heatmap  
- Target distribution  
- Age distribution  
- Cholesterol distribution  
- Resting BP distribution  
- Oldpeak boxplot  
- Feature importance bar chart  
- Pairplot  

These help understand which features contribute the most to heart disease.

---

## 🧪 Model Output
The model predicts:

- **1 → High chance of heart disease**  
- **0 → Low chance of heart disease**  



## 🚀 How to Run This Project Locally

### 1️⃣ Install dependencies:

### 2️⃣ Run the Streamlit app:


Your browser will open the app automatically.


## 🌐 Deployment (Streamlit Cloud)

how to deploy this project:

1. Push all files to GitHub  
2. Open Streamlit Cloud  
3. Connect your GitHub repo  
4. Select `app.py`  
5. Add `requirements.txt`  
6. Deploy 🚀  

---

## 🛠 Tech Stack
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Seaborn  
- Streamlit  
- Joblib  

---

## 👨‍🎓 Author
**Lalit Shinde**  
AIML Engineering Student  
Machine Learning & Data Science Enthusiast  

---

## ⭐ If you like this project
Give the repo a **star ⭐ on GitHub** — it motivates me!
