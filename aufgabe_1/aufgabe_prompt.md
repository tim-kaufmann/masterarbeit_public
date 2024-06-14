# Aufgabe
Create a function named `word_count` that takes a file path as an argument, reads the file content, and counts the number of times each word appears in the file. The function should return a dictionary where the keys are the words and the values are the number of times that word appears in the file. It should ignore case and remove punctuation. Finally, the dictionary items should be sorted in descending order by the number of times the word appears. If multiple words appear the same number of times, they should be sorted in ascending alphabetical order. The function need to handle the case where the file does not exist.

# 0S Prompt
Your task is to generate python code to solve the following problem. The generated code must be placed between the ```python and ```, and only one code block is allowed: 
Create a function named `word_count` that takes a file path as an argument, reads the file content, and counts the number of times each word appears in the file. The function should return a dictionary where the keys are the words and the values are the number of times that word appears in the file. It should ignore case and remove punctuation. Finally, the dictionary items should be sorted in descending order by the number of times the word appears. If multiple words appear the same number of times, they should be sorted in ascending alphabetical order. The function need to handle the case where the file does not exist.

You need to follow the function names or class names in the test cases. The generated code should not contain any test cases: 
class Testword_count:
    def test_word_count_basic_file(self, capfd, tmp_path):
        file_path = tmp_path / 'test_basic.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(""This is a basic test file with some common words."")
        word_count(file_path)
        captured = capfd.readouterr()
        assert "'this': 1\n'is': 1\n'a': 1\n'basic': 1\n'test': 1\n'file': 1\n'with': 1\n'some': 1\n'common': 1\n'words': 1\n" in captured.out
