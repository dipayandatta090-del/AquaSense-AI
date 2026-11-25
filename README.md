
# AquaSense AI
### River Water Quality Prediction using Machine Learning

AquaSense AI is a Streamlit-based web application for exploring river water quality data and predicting Biochemical Oxygen Demand (BOD) using an existing Random Forest Regression model.

## Features

- Interactive dashboard
- BOD prediction using five water-quality parameters
- Water-quality data visualization
- Model information and feature importance
- Dataset exploration
- Downloadable prediction results

## Technology Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- Plotly
- Joblib

## Project Structure

```text
AquaSense_AI/
├── app.py
├── config.py
├── requirements.txt
├── data/
│   └── water_dataX.csv
├── src/
│   ├── core.py
│   └── pdf_report.py
└── output/
    └── models/
        └── final_bod_random_forest_5_features.joblib
```

## Run Locally

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python -m streamlit run app.py
```

## Model Information

- Algorithm: Random Forest Regression
- Prediction target: BOD
- Input features: Five water-quality parameters
- Model: Existing trained model; no retraining is performed by the website.

## Deployment

The application can be deployed using Streamlit Community Cloud by connecting this GitHub repository and selecting `app.py` as the main file.

Ensure that the dataset and trained model are included in the deployment environment and that their redistribution is permitted.

## Disclaimer

AquaSense AI is an educational project. Its BOD predictions are estimates and are not a substitute for laboratory water-quality testing.
