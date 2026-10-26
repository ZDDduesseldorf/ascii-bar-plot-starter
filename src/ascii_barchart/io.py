import pandas as pd

def load_rows(data):
    
    df = pd.read_csv(data)
    
    rows = list(df.itertuples(index=False, name=None))
    
    return rows


rows = load_rows("data/points.csv")
print(rows)