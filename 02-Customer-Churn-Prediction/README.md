# 📉 Customer Churn Prediction & Retention Analysis

## 📌 Project Overview
This project builds a classification pipeline to predict customer churn for a telecom company and identifies the primary operational factors driving customer attrition.

## 🛠️ Data Preprocessing & Workflow
- **Data Leakage Prevention:** Performed `train_test_split` prior to mean imputation and feature scaling.
- **Handling Class Imbalance:** Applied `stratify=y` and leveraged `class_weight='balanced'` for distance and tree models.
- **Model Benchmarking:** Evaluated Logistic Regression, K-Nearest Neighbors, Decision Trees, and SVM models using Precision, Recall, F1-Score, and Confusion Matrices.

## 💡 Business Takeaways
- **Top Churn Risks:** Month-to-month contracts, Fiber Optic internet subscriptions, and Electronic Check payment methods.
- **Retention Drivers:** Long-term 2-year contracts, high tenure, and active add-on services (Online Security, Tech Support).