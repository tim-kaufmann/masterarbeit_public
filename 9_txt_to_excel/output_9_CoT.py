import openpyxl

def txt2excle(file_path):
    # Read the contents of the txt file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Create a new Excel workbook and select the active sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    
    # Iterate through the lines and split by tabs
    for row_idx, line in enumerate(lines):
        for col_idx, value in enumerate(line.strip().split('\t')):
            # Write each value to the corresponding cell in the Excel sheet
            sheet.cell(row=row_idx + 1, column=col_idx + 1, value=value)
    
    # Save the workbook as 'output.xlsx'
    workbook.save('output.xlsx')
