import os
import shutil
import pytest
from output_8_CoT import backup_folder


class Testbackup_folder:
    def test_backup_empty_folder(self, tmp_path):
        source_folder = tmp_path / "empty_folder"
        target_folder = tmp_path / "target_folder_empty"
        source_folder.mkdir()
        assert source_folder.exists()
        backup_folder(source_folder, target_folder)
        assert target_folder.exists()
        assert not os.listdir(target_folder)

    def test_backup_with_subfolders(self, tmp_path):
        source_folder = tmp_path / "source_with_subfolders"
        target_folder = tmp_path / "target_with_subfolders"
        (source_folder / "subfolder").mkdir(parents=True)
        assert source_folder.exists()
        backup_folder(source_folder, target_folder)
        assert target_folder.exists()

    def test_backup_existing_target_folder(self, tmp_path):
        source_folder = tmp_path / "source_folder"
        target_folder = tmp_path / "target_folder"
        source_folder.mkdir()
        target_folder.mkdir()
        assert source_folder.exists()
        assert target_folder.exists()
        backup_folder(source_folder, target_folder)
        assert target_folder.exists()

    def test_backup_to_temporary_folder(self, tmp_path):
        source_folder = tmp_path / "source_folder"
        target_folder = tmp_path / "target_folder_temp"
        source_folder.mkdir()
        assert source_folder.exists()
        backup_folder(source_folder, target_folder)
        assert target_folder.exists()

    def test_source_folder_contains_files(self, setup_test_folders):
        source_folder, target_folder = setup_test_folders
        file1 = source_folder / "file1.txt"
        file2 = source_folder / "subfolder" / "file2.txt"
        file1.write_text("这是文件1的内容。")
        file2.parent.mkdir(parents=True)
        file2.write_text("这是文件2的内容。")

        assert file1.exists()
        assert file2.exists()

        backup_folder(source_folder, target_folder)

        assert (target_folder / "file1.txt").exists()
        assert (target_folder / "subfolder" / "file2.txt").exists()

    def test_backup_with_different_file_types(self, setup_test_folders):
        source_folder, target_folder = setup_test_folders       
        file_txt = source_folder / "file.txt"
        file_csv = source_folder / "data.csv"
        file_py = source_folder / "script.py"

        file_txt.write_text("这是一个文本文件。")
        file_csv.write_text("CSV 数据在这里。")
        file_py.write_text("# Python 脚本内容。")

        assert file_txt.exists()
        assert file_csv.exists()
        assert file_py.exists()

        backup_folder(source_folder, target_folder)

        assert (target_folder / "file.txt").exists()
        assert (target_folder / "data.csv").exists()
        assert (target_folder / "script.py").exists()


    @pytest.fixture
    def setup_test_folders(self, tmp_path):
        source_folder = tmp_path / "source_folder"
        target_folder = tmp_path / "target_folder"
        source_folder.mkdir()
        target_folder.mkdir()
        yield source_folder, target_folder