# Aufgabe
Write a program to implement the following problem description:
Given an HTML text containing multiple English sentences, write a function get_top_k_words_from_html(html, k) that returns the top k words with the highest frequency of occurrence.

Write a function get_top_k_words_from_html(html, k), where the parameter html is a string containing HTML tags, and k is a positive integer. The function should return a list containing the top k words with the highest frequency of occurrence and their frequencies, sorted in descending order of frequency.

Examples:
Input: "<p>We are the world, we are the children.</p> <p>We are the ones who make a brighter day.</p> <p>So let's start giving.</p>"
Output: [('we', 3), ('are', 3), ('the', 3)]

Input: "<p>The quick brown fox jumps over the lazy dog.</p> <p>The quick brown fox jumps over the lazy dog.</p>"
Output: [('the', 4), ('brown', 2), ('quick', 2)]

Note:

Words are case-insensitive, i.e., "The" and "the" are considered the same word.
A word is defined as a string composed of letters and numbers, excluding punctuation.
The returned list should include all the top k words with the same frequency of occurrence and their frequencies.
You can use libraries to parse HTML text and use standard library functions or modules to assist in solving the problem.
Please implement the function get_top_k_words_from_html(html, k) to solve this problem.

# Prompt
Your task is to generate python code to solve the following problem. The generated code must be placed between the ```python and ```, and only one code block is allowed: 
Write a program to implement the following problem description:
Given an HTML text containing multiple English sentences, write a function get_top_k_words_from_html(html, k) that returns the top k words with the highest frequency of occurrence.

Write a function get_top_k_words_from_html(html, k), where the parameter html is a string containing HTML tags, and k is a positive integer. The function should return a list containing the top k words with the highest frequency of occurrence and their frequencies, sorted in descending order of frequency.

Examples:
Input: "<p>We are the world, we are the children.</p> <p>We are the ones who make a brighter day.</p> <p>So let's start giving.</p>"
Output: [('we', 3), ('are', 3), ('the', 3)]

Input: "<p>The quick brown fox jumps over the lazy dog.</p> <p>The quick brown fox jumps over the lazy dog.</p>"
Output: [('the', 4), ('brown', 2), ('quick', 2)]

Note:

Words are case-insensitive, i.e., "The" and "the" are considered the same word.
A word is defined as a string composed of letters and numbers, excluding punctuation.
The returned list should include all the top k words with the same frequency of occurrence and their frequencies.
You can use libraries to parse HTML text and use standard library functions or modules to assist in solving the problem.
Please implement the function get_top_k_words_from_html(html, k) to solve this problem.

You need to follow the function names or class names in the test cases. The generated code should not contain any test cases: 
class Testget_top_k_words_from_html:
    def test_empty_html(self):
        html = "<html><body></body></html>"
        assert get_top_k_words_from_html(html, 5) == []

