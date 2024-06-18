import openpyxl
import pandas as pd

def txt2excle(file_path):
    # Read the contents of the text file
    data = pd.read_csv(file_path, sep='\t', header=None)
    
    # Create a new Excel writer object
    writer = pd.ExcelWriter('output.xlsx', engine='openpyxl')
    
    # Write the data to the Excel file
    data.to_excel(writer, index=False, header=False)
    
    # Save the Excel file
    writer.save()
