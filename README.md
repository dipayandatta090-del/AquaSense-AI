# 💧 Smart Water Quality Prediction Using Machine Learning

### 🌍 An Intelligent Machine Learning Approach for Water Quality Assessment

**AquaSense AI** is a Machine Learning-based project designed to estimate **Biochemical Oxygen Demand (BOD)** using selected water quality parameters. It uses a **Random Forest Regression** model and an interactive **Streamlit** web application.

---

## 📌 1. Project Overview

Water is one of the most essential natural resources for human survival and environmental sustainability. However, increasing water pollution has become a serious global concern.

AquaSense AI analyzes selected water quality parameters and predicts BOD values using a trained Random Forest Regression model.

## 🚨 2. Problem Statement

Water pollution poses significant risks to aquatic ecosystems and environmental sustainability.

Traditional water quality assessment methods often require laboratory testing, specialized equipment, and time-consuming procedures.

The main objective of this project is to develop a predictive model that estimates **Biochemical Oxygen Demand (BOD)** from selected water quality parameters.

## 🎯 3. Project Objectives

- 💧 Predict Biochemical Oxygen Demand (BOD) using Machine Learning.
- 📊 Analyze water quality parameters through Exploratory Data Analysis.
- 🧹 Perform data cleaning and preprocessing.
- 🔍 Identify relevant input features.
- 🤖 Implement a Random Forest Regression model.
- 📈 Evaluate model performance using regression metrics.
- 💻 Develop an interactive web-based prediction application.

## 📂 4. Dataset Description

The project uses a water quality dataset containing physical and chemical parameters.

### Dataset Summary

| Dataset Information | Details |
|---|---|
| Dataset | Water Quality Dataset |
| Total Samples | 1,948* |
| Training Samples | 1,558* |
| Testing Samples | 390* |
| Input Features | 5 |
| Target Variable | BOD |
| Problem Type | Regression |

### Input Features

1. **pH**
2. **Dissolved Oxygen (D.O.)**
3. **Conductivity**
4. **Nitrate and Nitrite**
5. **Total Coliform**

**Target Variable:** Biochemical Oxygen Demand (BOD)

**Dataset Source:** Add the original dataset download link here.

## 🔬 5. Methodology

1. 📥 **Data Collection** – Obtain the water quality dataset.
2. 🧹 **Data Preprocessing** – Handle missing values and prepare the dataset.
3. 📊 **Exploratory Data Analysis** – Understand data distributions and relationships.
4. 🔍 **Feature Selection** – Use five selected water quality parameters.
5. ✂️ **Data Splitting** – Divide the dataset into training and testing sets.
6. 🤖 **Model Training** – Apply the Random Forest Regression algorithm.
7. 📈 **Model Evaluation** – Evaluate predictions using regression metrics.
8. 💾 **Model Saving** – Save the trained model for future predictions.
9. 🌐 **Web Application Development** – Integrate the trained model into a Streamlit application.

## 🧠 6. Machine Learning Algorithm

### 🌳 Random Forest Regressor

Random Forest is an ensemble Machine Learning algorithm that combines multiple decision trees to generate predictions.

**Advantages:**

- Handles nonlinear relationships.
- Combines predictions from multiple decision trees.
- Captures complex patterns in data.
- Provides feature-importance information.
- Supports numerical prediction tasks.

## ⚙️ 7. Technologies and Libraries Used

| Technology / Library | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning |
| Plotly | Interactive data visualization |
| Matplotlib | Data visualization |
| Joblib | Model serialization |
| Streamlit | Web application development |
| Jupyter Notebook | Model development and experimentation |

## 📈 8. Model Performance Evaluation

| Metric | Description | Model Result |
|---|---|---|
| R² Score | Measures how well the model explains variation in BOD | To be calculated |
| MAE | Mean Absolute Error | To be calculated |
| MSE | Mean Squared Error | To be calculated |
| RMSE | Root Mean Squared Error | To be calculated |

> **Note:** Actual test-set evaluation results should be added after verifying predictions against the corresponding test dataset.

## 📁 9. Project Repository Structure

```text
AquaSense_AI/
│
├── app.py
├── train.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── water_dataX.csv
│
├── src/
│   ├── core.py
│   └── pdf_report.py
│
├── notebooks/
│
├── output/
│   ├── figures/
│   └── models/
│       └── final_bod_random_forest_5_features.joblib
│
└── .streamlit/
    └── config.toml