from output_12_RP import list_files

class Testlist_files:
    def test_list_files_2(self, tmp_path, capsys):
        d = tmp_path / "sub"
        d.mkdir()
        p = d / "hello.txt"
        p.write_text("content")
        p2 = tmp_path / "world.txt"
        p2.write_text("content")
        list_files(tmp_path)
        captured = capsys.readouterr()
        assert 'world.txt' in captured.out and 'hello.txt' in captured.out

    def test_list_files_3(self, tmp_path, capsys):
        list_files(tmp_path)
        captured = capsys.readouterr()
        assert captured.out == ""

    def test_list_files_4(self, tmp_path, capsys):
        d = tmp_path / "sub"
        d.mkdir()
        p = d / "hello.txt"
        p.write_text("content")
        d2 = tmp_path / "sub2"
        d2.mkdir()
        p2 = d2 / "world.txt"
        p2.write_text("content")
        list_files(tmp_path)
        captured = capsys.readouterr()
        assert 'world.txt' in captured.out and 'hello.txt' in captured.out

    def test_list_files_5(self, tmp_path, capsys):
        d = tmp_path / "sub"
        d.mkdir()
        p = d / "hello.txt"
        p.write_text("content")
        d2 = d / "sub2"
        d2.mkdir()
        p2 = d2 / "world.txt"
        p2.write_text("content")
        list_files(tmp_path)
        captured = capsys.readouterr()
        assert 'world.txt' in captured.out and 'hello.txt' in captured.out

    def test_list_files_6(self, tmp_path, capsys):
        d = tmp_path / "sub"
        d.mkdir()
        p = d / "hello.txt"
        p.write_text("content")
        d2 = d / "sub2"
        d2.mkdir()
        p2 = d2 / "world.txt"
        p2.write_text("content")
        d3 = d2 / "sub3"
        d3.mkdir()
        p3 = d3 / "python.txt"
        p3.write_text("content")
        list_files(tmp_path)
        captured = capsys.readouterr()
        assert 'world.txt' in captured.out and 'hello.txt' in captured.out and 'python.txt' in captured.out

    def test_list_files_7(self, capsys):
        list_files("/invalid/path")
        captured = capsys.readouterr()
        assert 'Invalid directory path.' in captured.out