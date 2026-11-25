
import joblib
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

from pathlib import Path
from src.core import load_data


# ---------------------------------
# PROJECT PATHS
# ---------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA = BASE_DIR / "data" / "water_dataX.csv"

MODEL_PATH = (
    BASE_DIR / "output" / "models" /
    "final_bod_random_forest_5_features.joblib"
)


# ---------------------------------
# PAGE CONFIGURATION
# ---------------------------------

st.set_page_config(
    page_title="AquaSense AI",
    page_icon="💧",
    layout="wide"
)


# ---------------------------------
# CUSTOM DESIGN
# ---------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #F3F7FB;
}

[data-testid="stSidebar"] {
    background: #102A43;
}

[data-testid="stSidebar"] * {
    color: #EDF7FC;
}

.hero {
    background: linear-gradient(120deg,#102A43,#14566A,#07828D);
    padding: 30px 34px;
    border-radius: 18px;
    color: white;
    margin-bottom: 20px;
}

.hero h1 {
    color: white;
    font-size: 34px;
    font-weight: 800;
}

.hero p {
    color: #D7EEF1;
}

.eyebrow {
    color: #8DE1E5;
    font-size: 11px;
    letter-spacing: 2px;
    font-weight: 800;
}

div.stButton>button {
    background: #087E8B;
    color: white;
    border: 0;
    border-radius: 9px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)


def hero(tag, title, desc):
    st.markdown(
        f"""
        <div class="hero">
            <div class="eyebrow">{tag}</div>
            <h1>{title}</h1>
            <p>{desc}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------
# LOAD DATASET
# ---------------------------------

@st.cache_data
def get_data():
    if not DATA.exists():
        return None

    return load_data(DATA)


try:
    df = get_data()
except Exception as e:
    st.error(f"Dataset error: {e}")
    df = None


# ---------------------------------
# LOAD EXISTING BOD MODEL
# ---------------------------------

@st.cache_resource
def get_model():
    if not MODEL_PATH.exists():
        return None, None

    saved = joblib.load(MODEL_PATH)

    model = saved["model"]
    features = saved["features"]

    return model, features


try:
    model, features = get_model()
except Exception as e:
    model, features = None, None
    st.error(f"Model loading error: {e}")


ready = model is not None


# ---------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------

with st.sidebar:

    st.markdown("# 💧 AquaSense AI")

    st.caption("RIVER WATER QUALITY ANALYTICS")

    page = st.radio(
        "NAVIGATION",
        [
            "Dashboard",
            "Prediction",
            "Data Visualization",
            "Model Performance",
            "Dataset Explorer",
            "About Project"
        ]
    )

    st.divider()

    st.caption("STUDENT MACHINE LEARNING PROJECT")


# ---------------------------------
# DASHBOARD
# ---------------------------------

if page == "Dashboard":

    hero(
        "SMART WATER ANALYTICS",
        "Understand River Water Quality",
        "Explore water measurements and predict Biochemical Oxygen Demand using Machine Learning."
    )

    a, b, c, d = st.columns(4)

    a.metric(
        "Model Status",
        "Ready" if ready else "Not Found"
    )

    b.metric(
        "Algorithm",
        "Random Forest"
    )

    c.metric(
        "Input Features",
        len(features) if features else 0
    )

    d.metric(
        "Dataset Records",
        len(df) if df is not None else 0
    )

    st.subheader("Platform Overview")

    x, y = st.columns(2)

    with x:
        st.info(
            "Use the Prediction page to estimate BOD from five water-quality measurements."
        )

    with y:
        st.info(
            "Explore dataset patterns, missing values, correlations and model performance."
        )

    if df is not None:

        st.subheader("Dataset Preview")

        st.dataframe(
            df.head(10),
            use_container_width=True
        )


# ---------------------------------
# BOD PREDICTION
# ---------------------------------

elif page == "Prediction":

    hero(
        "PREDICTIVE ANALYTICS",
        "BOD Prediction",
        "Enter five water-quality measurements to estimate Biochemical Oxygen Demand."
    )

    if not ready:
        st.error("Existing BOD model could not be loaded.")
        st.stop()

    if df is None:
        st.error("Dataset not found in the data folder.")
        st.stop()

    st.info(
        "Enter the measured values of the five features used by your existing Random Forest model."
    )

    values = {}

    with st.form("bod_prediction_form"):

        cols = st.columns(2)

        for i, feature in enumerate(features):

            if feature in df.columns:
                series = pd.to_numeric(
                    df[feature], errors="coerce"
                ).dropna()

                default = (
                    float(series.median())
                    if not series.empty else 0.0
                )
            else:
                default = 0.0

            value = cols[i % 2].number_input(
                feature,
                value=default,
                format="%.4f"
            )

            values[feature] = value

        submit = st.form_submit_button(
            "Predict BOD",
            use_container_width=True
        )

    if submit:

        sample = pd.DataFrame(
            [values],
            columns=features
        )

        try:

            prediction = float(model.predict(sample)[0])

            st.subheader("Prediction Result")

            st.success(
                f"Estimated BOD: {prediction:.3f} mg/L"
            )

            st.metric(
                "Predicted BOD",
                f"{prediction:.3f} mg/L"
            )

            result = pd.DataFrame({
                "Feature": list(values.keys()),
                "Input Value": list(values.values())
            })

            st.subheader("Input Measurements")

            st.dataframe(
                result,
                use_container_width=True,
                hide_index=True
            )

            report = pd.DataFrame([{
                **values,
                "Predicted BOD (mg/L)": prediction
            }])

            st.download_button(
                "Download Prediction Report (CSV)",
                report.to_csv(index=False).encode("utf-8"),
                "aquasense_bod_prediction.csv",
                "text/csv"
            )

            st.caption(
                "Educational model estimate only. "
                "It is not a laboratory-certified water-quality result."
            )

        except Exception as e:

            st.error(f"Prediction failed: {e}")


# ---------------------------------
# DATA VISUALIZATION
# ---------------------------------

elif page == "Data Visualization":

    hero(
        "DATA EXPLORATION",
        "Discover Water Quality Patterns",
        "Explore distributions, relationships and correlations between water parameters."
    )

    if df is None:
        st.warning("water_dataX.csv was not found.")
        st.stop()

    numeric = df.select_dtypes(include="number")

    st.metric(
        "Dataset Size",
        f"{len(df):,} rows × {len(df.columns)} columns"
    )

    if len(numeric.columns) > 1:

        st.subheader("Correlation Heatmap")

        corr = numeric.corr()

        st.plotly_chart(
            px.imshow(
                corr,
                text_auto=".2f",
                color_continuous_scale="RdBu_r",
                title="Water Quality Parameter Correlation"
            ),
            use_container_width=True
        )

    if len(numeric.columns) > 0:

        feature = st.selectbox(
            "Select Water Quality Parameter",
            numeric.columns.tolist()
        )

        st.plotly_chart(
            px.histogram(
                df,
                x=feature,
                marginal="box",
                title=f"Distribution of {feature}",
                color_discrete_sequence=["#0B8994"]
            ),
            use_container_width=True
        )

        st.plotly_chart(
            px.box(
                df,
                y=feature,
                title=f"Outlier Analysis: {feature}",
                color_discrete_sequence=["#087E8B"]
            ),
            use_container_width=True
        )

    st.subheader("Statistical Summary")

    st.dataframe(
        numeric.describe().T,
        use_container_width=True
    )


# ---------------------------------
# MODEL PERFORMANCE
# ---------------------------------

elif page == "Model Performance":

    hero(
        "MODEL EVALUATION",
        "BOD Model Performance",
        "Evaluate the existing Random Forest regression model."
    )

    if not ready:
        st.warning("Existing BOD model not found.")
        st.stop()

    st.success("Existing Random Forest BOD model loaded.")

    st.metric(
        "Number of Input Features",
        len(features)
    )

    st.subheader("Model Input Features")

    st.write(features)

    if hasattr(model, "feature_importances_"):

        importance = pd.DataFrame({
            "Feature": features,
            "Importance": model.feature_importances_
        }).sort_values(
            "Importance",
            ascending=False
        )

        st.subheader("Feature Importance")

        st.plotly_chart(
            px.bar(
                importance,
                x="Importance",
                y="Feature",
                orientation="h",
                title="Importance of Water Quality Parameters",
                color="Importance",
                color_continuous_scale="Teal"
            ),
            use_container_width=True
        )

    st.info(
        "The existing model is loaded without retraining. "
        "Test-set regression metrics are not recalculated here."
    )


# ---------------------------------
# DATASET EXPLORER
# ---------------------------------

elif page == "Dataset Explorer":

    hero(
        "DATA MANAGEMENT",
        "Explore Your Dataset",
        "Inspect records, column types and missing values."
    )

    if df is None:
        st.warning("Dataset not found.")
        st.stop()

    a, b, c = st.columns(3)

    a.metric("Total Rows", f"{len(df):,}")

    b.metric("Total Columns", len(df.columns))

    c.metric(
        "Missing Cells",
        int(df.isna().sum().sum())
    )

    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(100),
        use_container_width=True
    )

    missing = (
        df.isna().sum()
        .rename("Missing Values")
        .reset_index()
    )

    missing.columns = ["Column", "Missing Values"]

    st.subheader("Missing Value Analysis")

    st.plotly_chart(
        px.bar(
            missing,
            x="Column",
            y="Missing Values",
            title="Missing Values by Column",
            color_discrete_sequence=["#0B8994"]
        ),
        use_container_width=True
    )

    st.subheader("Column Information")

    info = pd.DataFrame({
        "Column": df.columns,
        "Data Type": [str(t) for t in df.dtypes],
        "Non-null Values": [
            int(v) for v in df.notna().sum()
        ],
        "Missing Values": [
            int(v) for v in df.isna().sum()
        ]
    })

    st.dataframe(
        info,
        use_container_width=True
    )

    st.download_button(
        "Download Dataset CSV",
        df.to_csv(index=False).encode("utf-8"),
        "water_dataX_export.csv",
        "text/csv"
    )


# ---------------------------------
# ABOUT PROJECT
# ---------------------------------

else:

    hero(
        "PROJECT INFORMATION",
        "About AquaSense AI",
        "Machine Learning Based River Water Quality Analysis"
    )

    st.subheader("Problem Statement")

    st.write(
        "River water quality is affected by different physical, "
        "chemical and biological parameters. AquaSense AI uses "
        "machine learning to estimate Biochemical Oxygen Demand "
        "from selected water-quality measurements."
    )

    st.subheader("Project Objectives")

    st.markdown("""
    - Analyze river water-quality measurements.
    - Explore missing values and statistical patterns.
    - Estimate BOD using an existing Random Forest regression model.
    - Visualize relationships between water parameters.
    - Provide an interactive Streamlit web application.
    """)

    st.subheader("Machine Learning Model")

    st.write(
        "Random Forest Regressor"
    )

    st.subheader("Technology Stack")

    st.write("""
    - Python
    - Pandas and NumPy
    - Scikit-learn
    - Streamlit
    - Plotly
    - Joblib
    """)

    st.warning(
        "AquaSense AI is an educational prototype. "
        "Its predictions are not certified laboratory results "
        "or proof of drinking-water safety."
    )
