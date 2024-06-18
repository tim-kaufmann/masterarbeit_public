import openpyxl

def txt2excle(file_path):
    # Open the text file and read its contents
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Create a new Excel workbook and select the active worksheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Iterate through the lines and split by tab character
    for row_index, line in enumerate(lines):
        columns = line.strip().split('\t')
        for col_index, value in enumerate(columns):
            sheet.cell(row=row_index + 1, column=col_index + 1, value=value)

    # Save the workbook as 'output.xlsx'
    workbook.save('output.xlsx')
