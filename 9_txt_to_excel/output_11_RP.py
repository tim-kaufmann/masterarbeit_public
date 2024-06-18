import openpyxl

def txt2excle(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Create a new workbook and select the active worksheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Split the content by tabs and write to the sheet
    for row_idx, line in enumerate(lines):
        values = line.strip().split('\t')
        for col_idx, value in enumerate(values):
            sheet.cell(row=row_idx + 1, column=col_idx + 1, value=value)

    # Save the workbook
    workbook.save('output.xlsx')
