import os
from output_7_CoT import label_filter


class Testlabel_filter:
    def test_label_filter_2(self, tmpdir):
        p = tmpdir.mkdir("sub").join("test2.txt")
        p.write("1 0.5 0.5 0.5 0.5\n2 0.5 0.5 0.5 0.5\n3 0.5 0.5 0.5 0.5")
        label_filter(str(tmpdir / "sub"), [1,2,3])
        assert p.read() == ""

    def test_label_filter_3(self, tmpdir):
        p = tmpdir.mkdir("sub").join("test3.txt")
        p.write("0 0.5 0.5 0.5 0.5\n4 0.5 0.5 0.5 0.5")
        label_filter(str(tmpdir / "sub"), [1,2,3])
        assert p.read() == "0 0.5 0.5 0.5 0.5\n4 0.5 0.5 0.5 0.5\n"

    def test_label_filter_4(self, tmpdir):
        p = tmpdir.mkdir("sub").join("test4.txt")
        p.write("0 0.5 0.5 0.5 0.5\n1 0.5 0.5 0.5 0.5\n2 0.5 0.5 0.5 0.5\n3 0.5 0.5 0.5 0.5\n4 0.5 0.5 0.5 0.5")
        label_filter(str(tmpdir / "sub"), [0,4])
        assert p.read() == "1 0.5 0.5 0.5 0.5\n2 0.5 0.5 0.5 0.5\n3 0.5 0.5 0.5 0.5\n"

    def test_label_filter_5(self, tmpdir):
        p = tmpdir.mkdir("sub").join("test5.txt")
        p.write("0 0.5 0.5 0.5 0.5\n1 0.5 0.5 0.5 0.5\n2 0.5 0.5 0.5 0.5\n3 0.5 0.5 0.5 0.5\n4 0.5 0.5 0.5 0.5")
        label_filter(str(tmpdir / "sub"), [])
        assert p.read() == "0 0.5 0.5 0.5 0.5\n1 0.5 0.5 0.5 0.5\n2 0.5 0.5 0.5 0.5\n3 0.5 0.5 0.5 0.5\n4 0.5 0.5 0.5 0.5\n"

    def test_label_filter_6(self, tmpdir):
        p = tmpdir.mkdir("sub").join("test6.txt")
        p.write("0 0.5 0.5 0.5 0.5\n1 0.5 0.5 0.5 0.5\n2 0.5 0.5 0.5 0.5\n3 0.5 0.5 0.5 0.5\n4 0.5 0.5 0.5 0.5\n")
        label_filter(str(tmpdir / "sub"), [0,1,2,3,4])
        assert p.read() == ""

    def test_label_filter_7(self, tmpdir):
        p = tmpdir.mkdir("sub").join("test7.txt")
        p.write("0 0.5 0.5 0.5 0.5\n1 0.5 0.5 0.5 0.5\n2 0.5 0.5 0.5 0.5\n3 0.5 0.5 0.5 0.5\n4 0.5 0.5 0.5 0.5")
        label_filter(str(tmpdir / "sub"), [5,6,7])
        assert p.read() == "0 0.5 0.5 0.5 0.5\n1 0.5 0.5 0.5 0.5\n2 0.5 0.5 0.5 0.5\n3 0.5 0.5 0.5 0.5\n4 0.5 0.5 0.5 0.5\n"

    def test_label_filter_8(self, tmpdir):
        p = tmpdir.mkdir("sub").join("test8.txt")
        p.write("0 0.5 0.5 0.5 0.5\n1 0.5 0.5 0.5 0.5\n2 0.5 0.5 0.5 0.5\n3 0.5 0.5 0.5 0.5\n4 0.5 0.5 0.5 0.5")
        label_filter(str(tmpdir / "sub"), [0])
        assert p.read() == "1 0.5 0.5 0.5 0.5\n2 0.5 0.5 0.5 0.5\n3 0.5 0.5 0.5 0.5\n4 0.5 0.5 0.5 0.5\n"

    def test_label_filter_9(self, tmpdir):
        p = tmpdir.mkdir("sub").join("test9.txt")
        p.write("0 0.5 0.5 0.5 0.5\n1 0.5 0.5 0.5 0.5\n2 0.5 0.5 0.5 0.5\n3 0.5 0.5 0.5 0.5\n4 0.5 0.5 0.5 0.5")
        label_filter(str(tmpdir / "sub"), [4])
        assert p.read() == "0 0.5 0.5 0.5 0.5\n1 0.5 0.5 0.5 0.5\n2 0.5 0.5 0.5 0.5\n3 0.5 0.5 0.5 0.5\n"

    def test_label_filter_10(self, tmpdir):
        p = tmpdir.mkdir("sub").join("test10.txt")
        p.write("0 0.5 0.5 0.5 0.5\n1 0.5 0.5 0.5 0.5\n2 0.5 0.5 0.5 0.5\n3 0.5 0.5 0.5 0.5\n4 0.5 0.5 0.5 0.5")
        label_filter(str(tmpdir / "sub"), [0,1,2,3])
        assert p.read() == "4 0.5 0.5 0.5 0.5\n"
