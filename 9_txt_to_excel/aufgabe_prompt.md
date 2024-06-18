# Aufgabe
The list elements in the txt file are separated by tabs, convert the contents into an Excel spreadsheet.

# Prompt
Your task is to generate python code to solve the following problem. The generated code must be placed between the ```python and ```, and only one code block is allowed: 
The list elements in the txt file are separated by tabs, convert the contents into an Excel spreadsheet.

You need to follow the function names or class names in the test cases. The generated code should not contain any test cases: 
class Testtxt2excle:
    def test_txt2excle_1(self, tmp_path):
        file_path = tmp_path / "test1.txt"
        file_path.write_text("1\t2\t3\n4\t5\t6")
        txt2excle(file_path)
        workbook = openpyxl.load_workbook('output.xlsx')
        sheet = workbook.active
        assert sheet['A1'].value == '1'
        assert sheet['B1'].value == '2'
        assert sheet['C1'].value == '3'
        assert sheet['A2'].value == '4'
        assert sheet['B2'].value == '5'
        assert sheet['C2'].value == '6'