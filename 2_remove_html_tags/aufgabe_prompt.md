# Aufgabe
Define a function named remove_html_tags, which is used to remove HTML tags, comments, and document type declarations from the input string. Here is a description of the program's functionality and each step:

remove_html_tags function:

Purpose: Remove HTML tags, comments, and document type declarations from the input string.
Parameters:
s: The input string.
Return value:
The processed string, with HTML tags, comments, and document type declarations removed.
Main process:

First, check if the input is a string, if not, throw a ValueError.
If the input string is empty, return an empty string directly.
Define three regular expression patterns:
tag_pattern: Used to match HTML tags.
comment_pattern: Used to match HTML comments.
doctype_pattern: Used to match document type declarations.
Use the re.sub method to remove HTML comments, document type declarations, and HTML tags respectively.
Return the processed string. The processed string has HTML comments, document type declarations, and HTML tags removed, and also trims whitespace from both ends of the string.
This program uses regular expression patterns to perform multiple replacement operations on the input string, thereby achieving the function of removing HTML comments, document type declarations, and HTML tags.

# 0S Prompt
Your task is to generate python code to solve the following problem. The generated code must be placed between the ```python and ```, and only one code block is allowed: 
Define a function named remove_html_tags, which is used to remove HTML tags, comments, and document type declarations from the input string. Here is a description of the program's functionality and each step:

remove_html_tags function:

Purpose: Remove HTML tags, comments, and document type declarations from the input string.
Parameters:
s: The input string.
Return value:
The processed string, with HTML tags, comments, and document type declarations removed.
Main process:

First, check if the input is a string, if not, throw a ValueError.
If the input string is empty, return an empty string directly.
Define three regular expression patterns:
tag_pattern: Used to match HTML tags.
comment_pattern: Used to match HTML comments.
doctype_pattern: Used to match document type declarations.
Use the re.sub method to remove HTML comments, document type declarations, and HTML tags respectively.
Return the processed string. The processed string has HTML comments, document type declarations, and HTML tags removed, and also trims whitespace from both ends of the string.
This program uses regular expression patterns to perform multiple replacement operations on the input string, thereby achieving the function of removing HTML comments, document type declarations, and HTML tags.

You need to follow the function names or class names in the test cases. The generated code should not contain any test cases: 
class Testremove_html_tags:
    def test_basic_tags(self):
        html_string = ""<p>Hello, <strong>world!</strong></p>""
        assert remove_html_tags(html_string) == ""Hello, world!""

