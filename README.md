# 📊 Data Science & Machine Learning Portfolio

Welcome to my Machine Learning portfolio! This repository highlights end-to-end data science projects focused on data preprocessing, data leakage prevention, predictive modeling, model comparison, and business insights.

---

## 🚀 Featured Projects

### 1. 🏠 [California Property Price Prediction](./01-Property-Price-Prediction/)
* **Problem Type:** Regression Analysis
* **Goal:** Forecast district median house values across California using spatial and demographic variables.
* **Key Steps:** Handled missing values, standardized geographic coordinates (`StandardScaler`), applied One-Hot Encoding (`pd.get_dummies`), and trained Multiple Linear Regression models.
* **Evaluation:** Evaluated model performance using $R^2$ score and Mean Squared Error ($MSE$).

---

### 2. 📉 [Customer Churn Prediction](./02-Customer-Churn-Prediction/)
* **Problem Type:** Imbalanced Binary Classification
* **Goal:** Identify high-risk churn customers and extract key business drivers to reduce customer attrition.
* **Key Steps:** Built a leakage-free preprocessing pipeline (stratified split, mean imputation on train set only), balanced minority classes (`class_weight='balanced'`), and benchmarked four algorithms: Logistic Regression, K-Nearest Neighbors, Decision Trees, and Support Vector Machines.
* **Key Insights:** Extracted model coefficients to reveal that month-to-month contracts and fiber optic internet services are the top drivers of customer churn.

---

## 🛠️ Tech Stack & Tools
* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn
* **Data Visualization:** Seaborn, Matplotlib
* **Environment:** Jupyter Notebook




### 3. ❤️ [Heart Disease Risk Prediction App](./03-Heart-Disease-Prediction/)
* **Problem Type:** Binary Classification & Web Deployment
* **Goal:** Predict cardiovascular risk levels using patient vitals and biometric data, deployed as an interactive web dashboard.
* **Key Steps:** Built a data leakage-free `Pipeline` with `ColumnTransformer` (`StandardScaler` for continuous numerical features and `OneHotEncoder` for categorical parameters), trained baseline classifiers (Logistic Regression, KNN, Decision Tree, SVM), and deployed the optimal model via Streamlit.
* **Interactive Features:** Customized a dark navy dashboard UI featuring real-time BMI calculations and dynamic Plotly gauge chart visualizations for patient risk assessment.
* **Live App:** [View Live Streamlit Web App](YOUR_STREAMLIT_APP_URL_HERE)

## 🛠️ Tech Stack & Tools
* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn
* **Data Visualization:** Seaborn, Matplotlib, Plotly
* **Web Framework & Deployment:** Streamlit
* **Environment:** Jupyter Notebook, Anaconda Desktop