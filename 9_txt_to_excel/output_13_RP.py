import openpyxl
import os

def txt2excle(file_path):
    # Create a new Excel workbook and select the active sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    
    # Read the contents of the txt file
    with open(file_path, 'r') as file:
        for row_index, line in enumerate(file):
            # Split each line by tabs and write to the Excel sheet
            for col_index, value in enumerate(line.strip().split('\t')):
                sheet.cell(row=row_index + 1, column=col_index + 1, value=value)
    
    # Save the workbook to a file
    workbook.save('output.xlsx')
