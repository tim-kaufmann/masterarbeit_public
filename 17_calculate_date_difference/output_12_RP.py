import pandas as pd
from io import StringIO

def calculate_date_difference(csv_contents: str) -> int:
    # Read the CSV contents into a DataFrame
    df = pd.read_csv(StringIO(csv_contents))
    
    # Convert the 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Calculate the difference between the max and min dates
    date_difference = (df['Date'].max() - df['Date'].min()).days
    
    return date_difference
