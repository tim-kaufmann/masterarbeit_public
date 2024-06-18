import openpyxl

def txt2excle(file_path):
    # Create a new Excel workbook and select the active worksheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    
    # Read the contents of the txt file
    with open(file_path, 'r') as file:
        for row_index, line in enumerate(file):
            # Split the line by tabs
            values = line.strip().split('\t')
            for col_index, value in enumerate(values):
                # Write each value to the corresponding cell in the worksheet
                sheet.cell(row=row_index + 1, column=col_index + 1, value=value)
    
    # Save the workbook to 'output.xlsx'
    workbook.save('output.xlsx')
