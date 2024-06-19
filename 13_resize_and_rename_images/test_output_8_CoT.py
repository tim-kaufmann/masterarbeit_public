from PIL import Image
from output_8_CoT import resize_and_rename_images

class Testresize_and_rename_images:
    def test_resize_and_rename_images_2(self, capsys):
        resize_and_rename_images('./13_resize_and_rename_images/test2/input', 'test2/output', (1024, 768))
        captured = capsys.readouterr()
        assert captured.out == "Modified images resolutions:\n001.jpg: 1024 x 768\n002.jpg: 1024 x 768\n"

    def test_resize_and_rename_images_3(self, capsys):
        resize_and_rename_images('./13_resize_and_rename_images/test3/input', 'test3/output', (1920, 1080))
        captured = capsys.readouterr()
        assert captured.out == "Modified images resolutions:\n001.jpg: 1920 x 1080\n"

    def test_resize_and_rename_images_4(self, capsys):
        resize_and_rename_images('./13_resize_and_rename_images/test4/input', 'test4/output', (1280, 720))
        captured = capsys.readouterr()
        assert captured.out == "Modified images resolutions:\n001.jpg: 1280 x 720\n002.jpg: 1280 x 720\n003.jpg: 1280 x 720\n004.jpg: 1280 x 720\n005.jpg: 1280 x 720\n006.jpg: 1280 x 720\n007.jpg: 1280 x 720\n008.jpg: 1280 x 720\n"

    def test_resize_and_rename_images_5(self, capsys):
        resize_and_rename_images('./13_resize_and_rename_images/test5/input', 'test5/output', (1600, 900))
        captured = capsys.readouterr()
        assert captured.out == "Modified images resolutions:\n001.jpg: 1600 x 900\n002.jpg: 1600 x 900\n"

    def test_resize_and_rename_images_6(self, capsys):
        resize_and_rename_images('./13_resize_and_rename_images/test6/input', 'test6/output', (2560, 1440))
        captured = capsys.readouterr()
        assert captured.out == "Modified images resolutions:\n001.jpg: 2560 x 1440\n002.jpg: 2560 x 1440\n003.jpg: 2560 x 1440\n"

    def test_resize_and_rename_images_7(self, capsys):
        resize_and_rename_images('./13_resize_and_rename_images/test7/input', 'test7/output', (800, 600))
        captured = capsys.readouterr()
        assert captured.out == "Modified images resolutions:\n"
