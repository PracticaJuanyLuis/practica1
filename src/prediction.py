import joblib
import pandas as pd

def predict(model_path, input_csv, output_csv):
    model = joblib.load(model_path)
    X = pd.read_csv(input_csv)
    preds = model.predict(X)
    pd.DataFrame({"prediction": preds}).to_csv(output_csv, index=False)
    print("Predicciones guardadas en:", output_csv)

if __name__ == "__main__":
    model_path = "models/model.pkl"
    input_csv = "data/nuevos_datos.csv"
    output_csv = "predicciones.csv"
    predict(model_path, input_csv, output_csv)
