# ❤️ Heart Disease Prediction App

A **Random Forest-based machine learning app** to predict the risk of heart disease using patient health data. Built with **Python**, **scikit-learn**, and **Streamlit** for a modern and interactive user interface.  

---

## Features

- Predict heart disease risk based on 14+ health features  
- Modern, aesthetic Streamlit interface with sliders, dropdowns, and radio buttons  
- Provides prediction along with confidence level  
- Uses a trained **Random Forest Classifier**  
- Fully preprocessed data pipeline for accurate predictions  

---

## Dataset

- Original dataset: `heart.csv`  
- Preprocessing includes:  
  - Removing duplicate rows  
  - One-hot encoding categorical features  
  - Converting boolean columns to 0/1  
  - Scaling continuous numeric columns (optional for Random Forest)  
- Final processed dataset: `processed_heart.csv`  

---

## Requirements

- Python 3.8+  
- Install required packages:

```bash
pip install pandas numpy scikit-learn streamlit joblib
```

---

## Project Structure

```
heart-disease-prediction/
│
├── heart.csv                # Original dataset
├── processed_heart.csv      # Cleaned & preprocessed dataset
├── heart_rf_model.pkl       # Trained Random Forest model
├── 01_data_preprocessing.py # Preprocessing script/notebook
├── model_training.py        # Model training and evaluation script
├── app.py                   # Streamlit app for live prediction
└── README.md                # Project documentation
```



## How to Run

1. **Preprocess the dataset (optional)**  

```bash
python 01_data_preprocessing.py
```

2. **Train the Random Forest model (optional)**  

```bash
python model_training.py
```

3. **Run the Streamlit app**  

```bash
streamlit run app.py


4. **Enter your health details** in the app and click **Predict Heart Disease Risk**.  



## Model Evaluation

- **Accuracy:** ~73% on test data  
- Balanced performance for both classes (heart disease and no heart disease)  
- Confusion matrix shows good precision and recall for both classes  



## Future Improvements

- Hyperparameter tuning of Random Forest for higher accuracy  
- Dark mode and custom themes in the Streamlit app  
- Deploy the app online for public access  
- Add probability bar charts or risk levels for better visualization  


## 👨‍🎓 Author
**Lalit Shinde**  
AIML Engineering Student  
Machine Learning & Data Science Enthusiast  

---

## ⭐ If you like this project
Give the repo a **star ⭐ on GitHub** — it motivates me!
