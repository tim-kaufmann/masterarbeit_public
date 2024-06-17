# Aufgabe
Write a program to complete the task: Meteorological Data Analysis

Write a program to analyze and process temperature data.

Requirements:

Write a function extract_temperatures_from_text(text: str) -> List[float], which takes a text string as a parameter, extracts temperature data from the text, and returns it in the form of a list. Each line in the file contains a temperature value in Celsius.

Write a function calculate_average_temperature(temperatures: List[float]) -> float, which takes a list of temperature data as a parameter, calculates the average temperature, and returns it.

Write a function find_highest_temperature(temperatures: List[float]) -> float, which takes a list of temperature data as a parameter, finds the highest temperature in it, and returns it.

Write a function find_lowest_temperature(temperatures: List[float]) -> float, which takes a list of temperature data as a parameter, finds the lowest temperature in it, and returns it.

Use case:

python
text = "Beijing, -4℃\nShanghai, 3℃\nGuangzhou, 12℃\nChongqing, 8℃"

temperatures = extract_temperatures_from_text(text)
average_temp = calculate_average_temperature(temperatures)
highest_temp = find_highest_temperature(temperatures)
lowest_temp = find_lowest_temperature(temperatures)

print("Extracted temperature data:", temperatures)
print("Average temperature:", average_temp)
print("Highest temperature:", highest_temp)
print("Lowest temperature:", lowest_temp)


# Prompt
Your task is to generate python code to solve the following problem. The generated code must be placed between the ```python and ```, and only one code block is allowed: 
Write a program to complete the task: Meteorological Data Analysis

Write a program to analyze and process temperature data.

Requirements:

Write a function extract_temperatures_from_text(text: str) -> List[float], which takes a text string as a parameter, extracts temperature data from the text, and returns it in the form of a list. Each line in the file contains a temperature value in Celsius.

Write a function calculate_average_temperature(temperatures: List[float]) -> float, which takes a list of temperature data as a parameter, calculates the average temperature, and returns it.

Write a function find_highest_temperature(temperatures: List[float]) -> float, which takes a list of temperature data as a parameter, finds the highest temperature in it, and returns it.

Write a function find_lowest_temperature(temperatures: List[float]) -> float, which takes a list of temperature data as a parameter, finds the lowest temperature in it, and returns it.

Use case:

python
text = "Beijing, -4℃\nShanghai, 3℃\nGuangzhou, 12℃\nChongqing, 8℃"

temperatures = extract_temperatures_from_text(text)
average_temp = calculate_average_temperature(temperatures)
highest_temp = find_highest_temperature(temperatures)
lowest_temp = find_lowest_temperature(temperatures)

print("Extracted temperature data:", temperatures)
print("Average temperature:", average_temp)
print("Highest temperature:", highest_temp)
print("Lowest temperature:", lowest_temp)

You need to follow the function names or class names in the test cases. The generated code should not contain any test cases: 
class Testextract_temperatures_from_text:
    def test_extract_temperatures_from_text_with_temperatures(self):
        text = "北京，-4℃\n上海，3℃\n广州，12℃\n重庆，8℃"
        cities, temperatures = extract_temperatures_from_text(text)
        assert cities == ["北京", "上海", "广州", "重庆"]
        assert temperatures == [-4.0, 3.0, 12.0, 8.0]