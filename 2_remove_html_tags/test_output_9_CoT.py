import string
from collections import Counter
from output_9_CoT import word_count

class Testword_count:
    def test_word_count_case_sensitive_file(self, capfd, tmp_path):
        file_path = tmp_path / 'test_case_sensitive.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("Case case CASE")
        word_count(file_path)
        captured = capfd.readouterr()
        assert "'case': 3" in captured.out


    def test_word_count_punctuation_file(self, capfd, tmp_path):
        file_path = tmp_path / 'test_punctuation.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("This sentence has some punctuation, like commas and periods.")
        word_count(file_path)
        captured = capfd.readouterr()
        assert "'this': 1\n'sentence': 1\n'has': 1\n'some': 1\n'punctuation': 1\n'like': 1\n'commas': 1\n'and': 1\n'periods': 1\n" in captured.out


    def test_word_count_same_word_file(self, capfd, tmp_path):
        file_path = tmp_path / 'test_same_word_multiple_times.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("word word word word word")
        word_count(file_path)
        captured = capfd.readouterr()
        assert "'word': 5" in captured.out

    def test_word_count_different_words_file(self, capfd, tmp_path):
        file_path = tmp_path / 'test_different_words_same_count.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("apple banana orange")
        word_count(file_path)
        captured = capfd.readouterr()
        assert "'apple': 1\n'banana': 1\n'orange': 1\n" in captured.out

    def test_word_count_empty_file(self, capfd, tmp_path):
        file_path = tmp_path / 'test_empty_file.txt'
        open(file_path, 'w', encoding='utf-8').close()
        word_count(file_path)
        captured = capfd.readouterr()
        assert captured.out.strip() == ""
