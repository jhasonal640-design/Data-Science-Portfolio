Welcome to  y Project!!

# 🏠 California Property Price Prediction

## 📌 Project Overview
This project predicts median house values in California districts using features like median income, housing age, average rooms, and geographical coordinates.

## 🛠️ Data Preprocessing & Modeling
- Imputed missing values using training set statistics to prevent data leakage.
- Scaled spatial coordinates (`Latitude`, `Longitude`) using `StandardScaler`.
- Encoded categorical features into numeric formats using dummy variables.
- Trained Simple and Multiple Linear Regression models.

## 📈 Key Results
- Evaluated models using $R^2$ score and $MSE$.
- Spatial coordinates and median income proved to be the strongest predictors of property values.