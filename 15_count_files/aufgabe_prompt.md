# Aufgabe
There is a directory with multiple subdirectories, each subdirectory contains a different number of files. Please write a Python program to calculate the total number of files in this directory and print it out.

# Prompt
Your task is to generate python code to solve the following problem. The generated code must be placed between the ```python and ```, and only one code block is allowed: 
There is a directory with multiple subdirectories, each subdirectory contains a different number of files. Please write a Python program to calculate the total number of files in this directory and print it out.

You need to follow the function names or class names in the test cases. The generated code should not contain any test cases: 
class Testcount_files:
    def test_case1(self, tmpdir):
        p = tmpdir.mkdir("sub").join("hello.txt")
        p.write("content")
        assert count_files(tmpdir) == 1