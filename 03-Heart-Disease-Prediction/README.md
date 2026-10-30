# ❤️ CardioPredict: Heart Disease Risk Assessment App

An interactive Machine Learning web application built using Python, Scikit-Learn, and Streamlit that estimates cardiovascular risk based on patient clinical parameters and biometrics.

---

## 📌 Project Overview
* **Goal:** Predict heart disease risk (`High Risk` vs. `Low Risk`) using patient clinical vitals and demographic data.
* **Pipeline Strategy:** Applied `ColumnTransformer` and `Pipeline` to prevent data leakage—incorporating `StandardScaler` for numeric features and `OneHotEncoder` for categorical variables (`country`, `occupation`).
* **Models Evaluated:** Logistic Regression, K-Nearest Neighbors (KNN), Decision Tree, and Support Vector Machine (SVM).

---

## 🩺 Dataset Features
* **Vitals & Biometrics:** `age`, `ap_hi` (Systolic BP), `ap_lo` (Diastolic BP), `cholesterol`, `gluc`, `height`, `weight`
* **Demographics:** `country`, `occupation`

---

## 🛠️ Tech Stack & Libraries
* **Language:** Python
* **ML Library:** Scikit-Learn
* **Data Processing:** Pandas, NumPy
* **Visualization:** Plotly
* **Web Framework:** Streamlit