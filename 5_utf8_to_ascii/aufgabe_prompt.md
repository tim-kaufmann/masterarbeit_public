# Aufgabe
Write a program that implements the function of converting a string from UTF-8 encoding to ASCII encoding. The requirements are as follows:

Input a string (UTF-8 encoding).
The program will read the input string character by character and convert each character into the corresponding ASCII code.
Print out the converted ASCII codes one by one.
You can use an appropriate programming language to implement this function. Please note that multi-byte characters in UTF-8 encoding need to be specially handled to ensure correct conversion to the corresponding ASCII code. After calling the utf8_to_ascii function, an ASCII code list will be output, each element of which corresponds to the ASCII code of a character in the input string.

For example, if the input string is ""Hello World!"", after calling the utf8_to_ascii function, the following ASCII code list will be output:

[72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33]
Where the first element 72 corresponds to the ASCII code of the character H, the second element 101 corresponds to the ASCII code of the character e, and so on.

These ASCII codes can be further used for other operations, such as encryption, conversion, etc.


# Prompt
Your task is to generate python code to solve the following problem. The generated code must be placed between the ```python and ```, and only one code block is allowed: 
Write a program that implements the function of converting a string from UTF-8 encoding to ASCII encoding. The requirements are as follows:

Input a string (UTF-8 encoding).
The program will read the input string character by character and convert each character into the corresponding ASCII code.
Print out the converted ASCII codes one by one.
You can use an appropriate programming language to implement this function. Please note that multi-byte characters in UTF-8 encoding need to be specially handled to ensure correct conversion to the corresponding ASCII code. After calling the utf8_to_ascii function, an ASCII code list will be output, each element of which corresponds to the ASCII code of a character in the input string.

For example, if the input string is "Hello World!", after calling the utf8_to_ascii function, the following ASCII code list will be output:

[72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33]
Where the first element 72 corresponds to the ASCII code of the character H, the second element 101 corresponds to the ASCII code of the character e, and so on.

These ASCII codes can be further used for other operations, such as encryption, conversion, etc.

You need to follow the function names or class names in the test cases. The generated code should not contain any test cases: 
class Testutf8_to_ascii:
    def test_hello_world(self):
        assert utf8_to_ascii("Hello, World!") == [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
