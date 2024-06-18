import openpyxl

def txt2excle(file_path):
    import openpyxl
    from openpyxl import Workbook

    # Create a new workbook and select the active worksheet
    wb = Workbook()
    ws = wb.active

    # Read the text file
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by tab and append to worksheet
            ws.append(line.strip().split('\t'))

    # Save the workbook to an Excel file
    wb.save('output.xlsx')
