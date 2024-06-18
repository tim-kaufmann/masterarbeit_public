# Aufgabe
Filter the category in the annotation files of the yolo format dataset in the field of image processing, only retain the category labels in Label_category, and delete other category labels, operate on the original file. Enter the path of the annotation file folder of the yolo format dataset and the Label_category list.

# Prompt
Your task is to generate python code to solve the following problem. The generated code must be placed between the ```python and ```, and only one code block is allowed: 
Filter the category in the annotation files of the yolo format dataset in the field of image processing, only retain the category labels in Label_category, and delete other category labels, operate on the original file. Enter the path of the annotation file folder of the yolo format dataset and the Label_category list.

You need to follow the function names or class names in the test cases. The generated code should not contain any test cases: 
class Testlabel_filter:
    def test_label_filter_1(self, tmpdir):
        p = tmpdir.mkdir("sub").join("test1.txt")
        p.write("0 0.5 0.5 0.5 0.5\n1 0.5 0.5 0.5 0.5\n2 0.5 0.5 0.5 0.5\n3 0.5 0.5 0.5 0.5\n4 0.5 0.5 0.5 0.5")
        label_filter(str(tmpdir / "sub"), [1,2,3])
        assert p.read() == "0 0.5 0.5 0.5 0.5\n4 0.5 0.5 0.5 0.5\n"