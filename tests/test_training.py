import pandas as pd

def test_dataset_has_sales_column():
    df = pd.read_csv("data/dataset.csv")
    assert "Sales" in df.columns