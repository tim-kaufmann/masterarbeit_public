import re
from collections import Counter
from bs4 import BeautifulSoup
from output_13_RP import get_top_k_words_from_html


class Testget_top_k_words_from_html:
    def test_basic_html(self):
        html = "<html><body>This is a simple HTML text. Hello world!</body></html>"
        assert get_top_k_words_from_html(html, 3) == [('simple', 1), ('html', 1), ('text', 1)]

    def test_html_with_tags(self):
        html = "<html><body><h1>Title</h1><p> is a paragraph.</p></body></html>"
        assert get_top_k_words_from_html(html, 4) == [('title', 1), ('paragraph', 1)]

    def test_html_with_special_characters(self):
        html = "<html><body>Encoding: &#1632;&#1633;&#1634;</body></html>"
        assert get_top_k_words_from_html(html, 3) == [('encoding', 1), ('٠١٢', 1)]

    def test_html_with_unicode_characters(self):
        html = "<html><body>Unicode: àéîőű</body></html>"
        assert get_top_k_words_from_html(html, 4) == [('unicode', 1), ('àéîőű', 1)]

    def test_html_with_duplicate_words(self):
        html = "<html><body>Repeated words test. This is a test repeated words.</body></html>"
        assert get_top_k_words_from_html(html, 4) == [('repeated', 2), ('words', 2), ('test', 2)]

    def test_large_html(self):
        # Test with a large HTML content
        html = "<html><body>" + "word1 " * 1000 + "</body></html>"
        assert get_top_k_words_from_html(html, 1) == [('word1', 1000)]


    def test_html_with_numbers(self):
        html = "<html><body>Numbers: 123 456 789</body></html>"
        assert get_top_k_words_from_html(html, 3) == [('numbers', 1), ('123', 1), ('456', 1)]


    def test_html_with_unicode_characters_and_numbers(self):
        html = "<html><body>Unicode and numbers: àéîőű 12345</body></html>"
        assert get_top_k_words_from_html(html, 4) == [('unicode', 1), ('numbers', 1), ('àéîőű', 1), ('12345', 1)]
