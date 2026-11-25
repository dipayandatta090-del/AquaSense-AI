from pathlib import Path
ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "water_potability.csv"
OUT = ROOT / "output"
FIGURES = OUT / "figures"
MODELS = OUT / "models"
MODEL = MODELS / "aquasense_model.joblib"
META = MODELS / "metadata.json"
METRICS = OUT / "metrics.json"
TARGET = "Potability"
