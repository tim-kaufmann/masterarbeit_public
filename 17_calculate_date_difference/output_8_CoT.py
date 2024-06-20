import pandas as pd
from io import StringIO

def calculate_date_difference(csv_contents):
    # Use StringIO to read the CSV contents as if it were a file
    df = pd.read_csv(StringIO(csv_contents))
    
    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Calculate the difference in days between the max and min date
    date_diff = (df['Date'].max() - df['Date'].min()).days
    
    return date_diff
