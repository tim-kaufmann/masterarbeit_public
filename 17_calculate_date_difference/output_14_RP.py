import pandas as pd
from io import StringIO

def calculate_date_difference(csv_contents):
    # Read the CSV content into a pandas DataFrame
    df = pd.read_csv(StringIO(csv_contents))
    
    # Convert the 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Calculate the difference in days between the earliest and the latest date
    date_diff = (df['Date'].max() - df['Date'].min()).days
    
    return date_diff
