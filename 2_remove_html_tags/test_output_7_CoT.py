import re
from output_7_CoT import remove_html_tags

class Testremove_html_tags:
    def test_multiple_tags(self):
        html_string = "<h1>Title</h1><p>Paragraph</p>"
        assert remove_html_tags(html_string) == "TitleParagraph"

    def test_special_characters(self):
        html_string = '<a href="https://example.com">Click here</a>'
        assert remove_html_tags(html_string) == "Click here"

    def test_comments(self):
        html_string = "<p>Hello <!-- Comment -->world!</p>"
        assert remove_html_tags(html_string) == "Hello world!"

    def test_empty_tags(self):
        html_string = "<br/>"
        assert remove_html_tags(html_string) == ""

    def test_doctype_declaration(self):
        html_string = "<!DOCTYPE html><html><body>Hello, world!</body></html>"
        assert remove_html_tags(html_string) == "Hello, world!"

    def test_empty_string(self):
        html_string = ""
        assert remove_html_tags(html_string) == ""

    def test_nonstring_input(self):
        invalid_input = "123"
        assert remove_html_tags(invalid_input) == "123"
