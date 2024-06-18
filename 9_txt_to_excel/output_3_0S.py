import openpyxl

def txt2excle(file_path):
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    with open(file_path, 'r') as file:
        for row_idx, line in enumerate(file, start=1):
            for col_idx, value in enumerate(line.strip().split('\t'), start=1):
                sheet.cell(row=row_idx, column=col_idx, value=value)

    workbook.save('output.xlsx')
