     def test_word_count_nonexistent_file(self, capfd, tmp_path):
        file_path = tmp_path / 'nonexistent_file.txt'
        word_count(file_path)
        captured = capfd.readouterr()
        assert "Error: File" in captured.out