# Aufgabe
Create a Python class that accepts a path parameter. If the received path does not exist, output "Invalid directory path." If the received path exists, output the names of all files in this path and the names of all files in its subdirectories.

# Prompt
Your task is to generate python code to solve the following problem. The generated code must be placed between the ```python and ```, and only one code block is allowed: 
Create a Python class that accepts a path parameter. If the received path does not exist, output "Invalid directory path." If the received path exists, output the names of all files in this path and the names of all files in its subdirectories.

You need to follow the function names or class names in the test cases. The generated code should not contain any test cases: 
class Testlist_files:
    def test_list_files_1(self, tmp_path, capsys):
        d = tmp_path / "sub"
        d.mkdir()
        p = d / "hello.txt"
        p.write_text("content")
        list_files(tmp_path)
        captured = capsys.readouterr()
        assert captured.out == "hello.txt\n"