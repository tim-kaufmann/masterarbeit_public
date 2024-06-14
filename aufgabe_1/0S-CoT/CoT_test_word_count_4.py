# test_word_count.py

from pathlib import Path
from pytest import CaptureFixture
from word_count_4 import word_count


class Testword_count:
    def test_word_count_case_sensitive_file(self, capfd: CaptureFixture[str], tmp_path: Path):
        file_path = tmp_path / 'test_case_sensitive.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("Case case CASE")
        word_count(file_path)
        captured = capfd.readouterr()
        assert "'case': 3" in captured.out

    def test_word_count_punctuation_file(self, capfd: CaptureFixture[str], tmp_path: Path):
        file_path = tmp_path / 'test_punctuation.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("This sentence has some punctuation, like commas and periods.")
        word_count(file_path)
        captured = capfd.readouterr()
        expected_output = (
            "'this': 1\n"
            "'sentence': 1\n"
            "'has': 1\n"
            "'some': 1\n"
            "'punctuation': 1\n"
            "'like': 1\n"
            "'commas': 1\n"
            "'and': 1\n"
            "'periods': 1\n"
        )
        assert expected_output in captured.out

    def test_word_count_same_word_file(self, capfd: CaptureFixture[str], tmp_path: Path):
        file_path = tmp_path / 'test_same_word_multiple_times.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("word word word word word")
        word_count(file_path)
        captured = capfd.readouterr()
        assert "'word': 5" in captured.out

    def test_word_count_different_words_file(self, capfd: CaptureFixture[str], tmp_path: Path):
        file_path = tmp_path / 'test_different_words_same_count.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("apple banana orange")
        word_count(file_path)
        captured = capfd.readouterr()
        expected_output = (
            "'apple': 1\n"
            "'banana': 1\n"
            "'orange': 1\n"
        )
        assert expected_output in captured.out

    def test_word_count_nonexistent_file(self, capfd: CaptureFixture[str], tmp_path: Path):
        file_path = tmp_path / 'nonexistent_file.txt'
        word_count(file_path)
        captured = capfd.readouterr()
        assert "Error: File" in captured.out

    def test_word_count_empty_file(self, capfd: CaptureFixture[str], tmp_path: Path):
        file_path = tmp_path / 'test_empty_file.txt'
        open(file_path, 'w', encoding='utf-8').close()
        word_count(file_path)
        captured = capfd.readouterr()
        assert captured.out.strip() == ""
