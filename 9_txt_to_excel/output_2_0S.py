import openpyxl

def txt2excle(file_path):
    # Read the contents of the text file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Create a new Excel workbook and select the active worksheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Populate the worksheet with the contents of the text file
    for row_idx, line in enumerate(lines):
        values = line.strip().split('\t')
        for col_idx, value in enumerate(values):
            sheet.cell(row=row_idx + 1, column=col_idx + 1, value=value)

    # Save the workbook to an Excel file
    workbook.save('output.xlsx')
