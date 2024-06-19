import os

class Testlist_files:
    def list_files(self, path):
        if not os.path.exists(path):
            print("Invalid directory path.")
        else:
            for root, dirs, files in os.walk(path):
                for file in files:
                    print(file)
                    
    def test_list_files_1(self, tmp_path, capsys):
        d = tmp_path / "sub"
        d.mkdir()
        p = d / "hello.txt"
        p.write_text("content")
        self.list_files(tmp_path)
        captured = capsys.readouterr()
        assert captured.out == "hello.txt\n"
