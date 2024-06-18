import openpyxl
import pandas as pd

def txt2excle(file_path):
    # Read the contents of the txt file
    data = pd.read_csv(file_path, sep='\t', header=None)
    
    # Write the data to an Excel file
    data.to_excel('output.xlsx', index=False, header=False)
