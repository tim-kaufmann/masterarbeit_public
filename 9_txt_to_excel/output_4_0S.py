import openpyxl

def txt2excle(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    workbook = openpyxl.Workbook()
    sheet = workbook.active

    for row_index, line in enumerate(lines):
        columns = line.strip().split('\t')
        for col_index, value in enumerate(columns):
            sheet.cell(row=row_index+1, column=col_index+1, value=value)

    workbook.save('output.xlsx')
