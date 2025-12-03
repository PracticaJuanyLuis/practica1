import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def load_data(path: str):
    return pd.read_csv(path)

def train_model(data_path: str, model_path: str):
    df = load_data(data_path)

    # La columna objetivo es Sales
    X = df.drop(columns=["Sales"])
    y = df["Sales"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)

    print("Modelo entrenado y guardado en:", model_path)

if __name__ == "__main__":
    data_path = "data/dataset.csv"
    model_path = "models/model.pkl"
    train_model(data_path, model_path)
