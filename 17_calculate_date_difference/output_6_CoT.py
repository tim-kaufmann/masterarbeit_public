import pandas as pd
from io import StringIO

def calculate_date_difference(csv_contents):
    # Load the CSV contents into a DataFrame
    df = pd.read_csv(StringIO(csv_contents))
    
    # Convert the Date column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Find the earliest and the latest dates
    earliest_date = df['Date'].min()
    latest_date = df['Date'].max()
    
    # Calculate the difference in days between the earliest and latest dates
    difference_in_days = (latest_date - earliest_date).days
    
    return difference_in_days
