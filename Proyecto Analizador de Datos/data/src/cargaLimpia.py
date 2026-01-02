import pandas as pd

def cargaData(path):
    df = pd.read_csv(path)
    df["fecha"] = pd.to_datetime(df["fecha"])
    return df
