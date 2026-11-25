💧 Smart Water Quality Prediction Using Machine Learning
🌍 An Intelligent Machine Learning Approach for Water Quality Assessment
AquaSense AI is a machine learning-based project that estimates
Biochemical Oxygen Demand (BOD) using selected water quality
parameters. It uses a Random Forest Regression model and an
interactive Streamlit web application to make BOD prediction and
data exploration easier.
📌 1. Project Overview
Water is one of the most essential natural resources for human survival
and environmental sustainability. However, increasing water pollution
has become a serious global concern.

AquaSense AI analyzes selected water quality parameters and predicts BOD
values using a trained Random Forest Regression model. The project
demonstrates how machine learning can support data-driven water quality
assessment.
🚨 2. Problem Statement
Water pollution poses significant risks to aquatic ecosystems and
environmental sustainability.

Traditional water quality assessment methods often require laboratory
testing, specialized equipment, and time-consuming procedures. An
intelligent, data-driven approach can help estimate important water
quality indicators from available measurements.

The main objective of this project is to develop a predictive model that
estimates Biochemical Oxygen Demand (BOD) from selected water
quality parameters.
🎯 3. Project Objectives
- 💧 Predict Biochemical Oxygen Demand (BOD) using Machine Learning.
- 📊 Analyze water quality parameters through Exploratory Data
  Analysis.
- 🧹 Perform data cleaning and preprocessing.
- 🔍 Identify relevant input features.
- 🤖 Implement a Random Forest Regression model.
- 📈 Evaluate model performance using regression metrics.
- 💻 Develop an interactive web-based prediction application.
📂 4. Dataset Description
The project uses a water quality dataset containing physical and
chemical parameters.
Dataset Summary
  Dataset Information                   Details
  Dataset                 Water Quality Dataset
Total samples                         1,948*
Training samples                      1,558*
Testing samples                         390*
Input features                              5
Target variable                           BOD
Problem type                       Regression

The sample counts above must be confirmed against the exact dataset and
training split used for the final model.
Input Features
The model uses the following five water quality parameters:
1. pH
2. Dissolved Oxygen (D.O.)
3. Conductivity
4. Nitrate and Nitrite
5. Total Coliform
Target Variable: Biochemical Oxygen Demand (BOD)

Dataset Source: Add the original dataset download link here.
🔬 5. Methodology
The project follows these implementation stages:
1. 📥 Data Collection -- Obtain the water quality dataset.
2. 🧹 Data Preprocessing -- Handle missing values and prepare the
   dataset.
3. 📊 Exploratory Data Analysis -- Understand data distributions
   and relationships.
4. 🔍 Feature Selection -- Use five selected water quality
   parameters.
5. ✂️ Data Splitting -- Divide the dataset into training and
   testing sets.
6. 🤖 Model Training -- Apply the Random Forest Regression
   algorithm.
7. 📈 Model Evaluation -- Evaluate predictions using regression
   metrics.
8. 💾 Model Saving -- Save the trained model for future
   predictions.
9. 🌐 Web Application Development -- Integrate the trained model
   into a Streamlit application.
🧠 6. Machine Learning Algorithm
🌳 Random Forest Regressor
Random Forest is an ensemble machine learning algorithm that combines
multiple decision trees to generate predictions.

In this project, Random Forest Regression is used to estimate BOD values
from the five selected water quality parameters.

Advantages:
- Handles nonlinear relationships.
- Combines predictions from multiple decision trees.
- Can capture complex patterns in data.
- Provides feature-importance information.
- Supports numerical prediction tasks.
⚙️ 7. Technologies and Libraries Used
  Technology / Library   Purpose
  Python                 Programming language
Pandas                 Data manipulation
NumPy                  Numerical operations
Scikit-learn           Machine learning and model development
Plotly                 Interactive data visualization
Matplotlib             Data visualization
Joblib                 Model serialization
Streamlit              Web application development
Jupyter Notebook       Model development and experimentation
📈 8. Model Performance Evaluation
The Random Forest Regression model can be evaluated using the following
regression metrics:
  Metric                Description                           Model Result
  R² Score              Measures how well the             To be calculated
model explains
variation in BOD      

  MAE                   Mean Absolute Error               To be calculated

  MSE                   Mean Squared Error                To be calculated
RMSE                  Root Mean Squared                 To be calculated
Error
Note: Actual test-set evaluation results should be added after
verifying predictions against the corresponding test dataset. Do not
enter estimated or unverified values.

📁 9. Project Repository Structure
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
Update this tree if your actual project folder contains different files
or folders.
🚀 10. Installation and Execution
Follow these steps to run the project locally.
Step 1: Clone the Repository
git clone https://github.com/dipayandatta090-del/AquaSense-AI.git
Step 2: Navigate to the Project Folder
cd AquaSense-AI
Step 3: Install the Required Libraries
pip install -r requirements.txt
Step 4: Run the Streamlit Application
python -m streamlit run app.py
The application will open in your web browser.
🌐 11. Application Features
- 📊 Interactive Dashboard
- 💧 BOD Prediction
- 📈 Data Visualization
- 🧠 Model Performance Overview
- 📂 Dataset Explorer
- 📄 PDF Report Generation (if enabled in the application)
🔮 12. Future Enhancements
- 🤖 Compare multiple machine learning algorithms.
- 📈 Improve prediction performance through hyperparameter tuning.
- 💧 Include additional water quality parameters.
- 🌐 Deploy the application for public access.
- 📊 Develop real-time water quality monitoring capabilities.
🏁 13. Conclusion
This project demonstrates how machine learning can be applied to
environmental monitoring through the prediction of Biochemical Oxygen
Demand (BOD).

By analyzing selected water quality parameters and developing a Random
Forest Regression model, AquaSense AI explores an intelligent approach
to water quality assessment. The project provides a foundation for
further development of automated and data-driven environmental
monitoring solutions.
👨‍💻 14. Project Information
  Field                               Details
  Project Title                   Smart Water Quality Prediction
Using Machine Learning

  Project Name                    AquaSense AI

  Project Domain                  Machine Learning / Environmental
Monitoring

  Project Type                    Academic Project

  Institution                     Ghani Khan Choudhury Institute of
Engineering and Technology

  Department                      Computer Science and Engineering

  Algorithm                       Random Forest Regression
Target Variable                 Biochemical Oxygen Demand (BOD)
⭐ If you find this project interesting, feel free to explore the
repository!