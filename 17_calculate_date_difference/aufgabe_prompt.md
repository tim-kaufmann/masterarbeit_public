# Aufgabe
Given a the contents of a CSV file as csv_contents, return the difference in days between the date of the earliest and the oldest entry.
The CSV file starts with a header row, which contains at least one column called Date.
You are optionally provided with the pandas library if you need it.  show me the code regarding to this question.

# Prompt
Your task is to generate python code to solve the following problem. The generated code must be placed between the ```python and ```, and only one code block is allowed: 
Given a the contents of a CSV file as csv_contents, return the difference in days between the date of the earliest and the oldest entry.

The CSV file starts with a header row, which contains at least one column called Date.

You are optionally provided with the pandas library if you need it.  show me the code regarding to this question.

You need to follow the function names or class names in the test cases. The generated code should not contain any test cases: 
class Testcalculate_date_difference:
    def test_calculate_date_difference_1(self):
        csv_contents = "Date\n2020-01-01\n2020-01-02\n2020-01-03"
        assert calculate_date_difference(csv_contents) == 2