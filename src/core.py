
import joblib
import pandas as pd



def load_data(source):
    try:
        df = pd.read_csv(source, encoding="utf-8-sig")
    except UnicodeDecodeError:
        df = pd.read_csv(source, encoding="cp1252")

    df = df.dropna(how="all").dropna(axis=1, how="all")

    if df.empty:
        raise ValueError("CSV dataset is empty.")

    return df



def load_bod_model(model_path):
    saved_data = joblib.load(model_path)

    model = saved_data["model"]
    features = saved_data["features"]

    return model, features


def prepare_bod_input(values, features):
    """
    Prepare user input in the exact feature order
    expected by the existing BOD model.
    """

    sample = pd.DataFrame([values], columns=features)

    return sample


def predict_bod(model, values, features):
    sample = prepare_bod_input(values, features)

    prediction = model.predict(sample)[0]

    return float(prediction)


def get_dataset_summary(df):
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isna().sum().sum()),
        "numeric_columns": list(
            df.select_dtypes(include="number").columns
        )
    }
