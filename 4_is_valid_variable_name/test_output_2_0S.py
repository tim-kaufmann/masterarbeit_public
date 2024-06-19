import re
from output_2_0S import is_valid_variable_name


class Testis_valid_variable_name:
    def test_is_valid_variable_name1(self):
        assert is_valid_variable_name('_bar') == True

    def test_is_valid_variable_name2(self):
        assert is_valid_variable_name('$baz') == True

    def test_is_valid_variable_name3(self):
        assert is_valid_variable_name('12abc') == False

    def test_is_valid_variable_name4(self):
        assert is_valid_variable_name('abc12') == True

    def test_is_valid_variable_name5(self):
        assert is_valid_variable_name('a' * 256) == False

    def test_is_valid_variable_name6(self):
        assert is_valid_variable_name(' ') == False

    def test_is_valid_variable_name7(self):
        assert is_valid_variable_name('foo bar') == False