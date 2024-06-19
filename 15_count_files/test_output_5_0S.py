import os
from output_5_0S import count_files

class Testcount_files:
    def test_case2(self, tmpdir):
        p1 = tmpdir.mkdir("sub1").join("hello.txt")
        p1.write("content")
        p2 = tmpdir.mkdir("sub2").join("world.txt")
        p2.write("content")
        assert count_files(tmpdir) == 2

    def test_case3(self, tmpdir):
        p1 = tmpdir.mkdir("sub1").join("hello.txt")
        p1.write("content")
        p2 = tmpdir.mkdir("sub2").join("world.txt")
        p2.write("content")
        p3 = tmpdir.mkdir("sub3").join("file.txt")
        p3.write("content")
        assert count_files(tmpdir) == 3

    def test_case4(self, tmpdir):
        p1 = tmpdir.mkdir("sub1").join("hello.txt")
        p1.write("content")
        p2 = tmpdir.mkdir("sub2").join("world.txt")
        p2.write("content")
        assert count_files(tmpdir) == 2

    def test_case5(self, tmpdir):
        assert count_files(tmpdir) == 0

    def test_case6(self, tmpdir):
        p1 = tmpdir.mkdir("sub1").join("hello.txt")
        p1.write("content")
        p2 = tmpdir.mkdir("sub2").join("world.txt")
        p2.write("content")
        p3 = tmpdir.mkdir("sub3").join("file.txt")
        p3.write("content")
        p4 = tmpdir.mkdir("sub4").join("example.txt")
        p4.write("content")
        assert count_files(tmpdir) == 4

    # Boundary test cases
    def test_case7(self, tmpdir):
        for i in range(100):
            p = tmpdir.mkdir(f"sub{i}").join("file.txt")
            p.write("content")
        assert count_files(tmpdir) == 100

    def test_case8(self, tmpdir):
        for i in range(1000):
            p = tmpdir.mkdir(f"sub{i}").join("file.txt")
            p.write("content")
        assert count_files(tmpdir) == 1000

    def test_case9(self, tmpdir):
        for i in range(500):
            p = tmpdir.mkdir(f"sub{i}").join("file.txt")
            p.write("content")
        assert count_files(tmpdir) == 500

    def test_case10(self, tmpdir):
        for i in range(10000):
            p = tmpdir.mkdir(f"sub{i}").join("file.txt")
            p.write("content")
        assert count_files(tmpdir) == 10000