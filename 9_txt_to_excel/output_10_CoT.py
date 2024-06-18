import openpyxl
import pandas as pd

def txt2excle(file_path):
    # Read the tab-separated file into a DataFrame
    df = pd.read_csv(file_path, delimiter='\t', header=None)
    
    # Create a new Excel writer object
    writer = pd.ExcelWriter('output.xlsx', engine='openpyxl')
    
    # Write the DataFrame to the Excel file
    df.to_excel(writer, index=False, header=False)
    
    # Save the Excel file
    writer.save()
