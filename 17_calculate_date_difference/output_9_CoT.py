import pandas as pd
from io import StringIO

def calculate_date_difference(csv_contents: str) -> int:
    # Read the CSV contents into a pandas DataFrame
    df = pd.read_csv(StringIO(csv_contents))
    
    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Find the earliest and latest dates
    earliest_date = df['Date'].min()
    latest_date = df['Date'].max()
    
    # Calculate the difference in days
    date_difference = (latest_date - earliest_date).days
    
    return date_difference
