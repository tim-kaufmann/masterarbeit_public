import openpyxl

def txt2excle(file_path):
    # Read the contents of the txt file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Create a new workbook and select the active worksheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Process each line and write to the Excel sheet
    for row_idx, line in enumerate(lines, start=1):
        values = line.strip().split('\t')
        for col_idx, value in enumerate(values, start=1):
            sheet.cell(row=row_idx, column=col_idx, value=value)

    # Save the workbook to an Excel file
    workbook.save('output.xlsx')
