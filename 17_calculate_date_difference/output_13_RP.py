import pandas as pd
from io import StringIO

def calculate_date_difference(csv_contents):
    df = pd.read_csv(StringIO(csv_contents))
    df['Date'] = pd.to_datetime(df['Date'])
    earliest_date = df['Date'].min()
    latest_date = df['Date'].max()
    difference_in_days = (latest_date - earliest_date).days
    return difference_in_days
