import openpyxl

def txt2excle(file_path):
    # Create a new workbook and select the active worksheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Open the text file and read its contents
    with open(file_path, 'r') as file:
        for row_idx, line in enumerate(file):
            values = line.strip().split('\t')
            for col_idx, value in enumerate(values):
                sheet.cell(row=row_idx + 1, column=col_idx + 1, value=value)

    # Save the workbook to an Excel file
    workbook.save('output.xlsx')
