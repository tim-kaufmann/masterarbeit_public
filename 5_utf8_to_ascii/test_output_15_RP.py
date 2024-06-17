from output_15_RP import utf8_to_ascii

class Testutf8_to_ascii:
    def test_empty_string(self):
        assert utf8_to_ascii("") == None

    def test_invalid_hex_code(self):
        assert utf8_to_ascii("Hello%20Wo%zz") == None

    def test_single_character(self):
        assert utf8_to_ascii("A") == [65]

    def test_special_characters(self):
        assert utf8_to_ascii("!@#$%^&*()_+-=") == [33, 64, 35, 36, 37, 94, 38, 42, 40, 41, 95, 43, 45, 61]

    def test_unicode_characters(self):
        assert utf8_to_ascii("\u2018\u2019\u201c\u201d") == [8216, 8217, 8220, 8221]

    def test_long_string(self):
        assert utf8_to_ascii("a" * 1000) == [97] * 1000

    def test_invalid_input_type(self):
        assert utf8_to_ascii(123) == None

    def test_invalid_input_encoding(self):
        assert utf8_to_ascii(b"Hello%20World%21") == None