import pandas as pd
from io import StringIO
from datetime import datetime

def calculate_date_difference(csv_contents: str) -> int:
    # Read the CSV contents into a DataFrame
    df = pd.read_csv(StringIO(csv_contents))
    
    # Convert the Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Find the earliest and the latest date
    min_date = df['Date'].min()
    max_date = df['Date'].max()
    
    # Calculate the difference in days
    date_difference = (max_date - min_date).days
    
    return date_difference
