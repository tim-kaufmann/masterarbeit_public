import pandas as pd
from io import StringIO

def calculate_date_difference(csv_contents: str) -> int:
    df = pd.read_csv(StringIO(csv_contents))
    df['Date'] = pd.to_datetime(df['Date'])
    min_date = df['Date'].min()
    max_date = df['Date'].max()
    date_difference = (max_date - min_date).days
    return date_difference
