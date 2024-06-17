from typing import List, Tuple
from output_9_CoT import extract_temperatures_from_text, calculate_average_temperature, find_highest_temperature, find_lowest_temperature

class Testextract_temperatures_from_text:
    def test_extract_temperatures_from_text_without_temperatures(self):
        text = "北京\n上海\n广州\n重庆"
        temperatures = extract_temperatures_from_text(text)
        assert temperatures == []

    def test_calculate_average_temperature(self):
        temperatures = [10.0, 20.0, 30.0]
        assert calculate_average_temperature(temperatures) == 20.0

    def test_find_highest_temperature(self):
        temperatures = [-4.0, 3.0, 12.0, 8.0]
        assert find_highest_temperature(temperatures) == (12.0)

    def test_find_lowest_temperature(self):
        temperatures = [-4.0, 3.0, 12.0, 8.0]
        assert find_lowest_temperature(temperatures) == (-4.0)

    def test_extract_temperatures_from_text_with_single_data(self):
        text = "北京，-4℃"
        temperatures = extract_temperatures_from_text(text)
        assert temperatures == [-4.0]

    def test_extract_temperatures_from_text_with_cities_only(self):
        text = "北京\n上海\n广州\n重庆"
        temperatures = extract_temperatures_from_text(text)
        assert temperatures == []

    def test_calculate_average_temperature_with_single_temperature(self):
        temperatures = [10.0]
        assert calculate_average_temperature(temperatures) == 10.0

    def test_find_highest_temperature_with_single_temperature(self):
        temperatures = [-4.0]
        assert find_highest_temperature(temperatures) == (-4.0)

    def test_find_lowest_temperature_with_single_temperature(self):
        temperatures = [-4.0]
        assert find_lowest_temperature(temperatures) == (-4.0)

    def test_extract_temperatures_from_text_with_duplicate_temperatures(self):
        text = "北京，-4℃\n上海, 3℃\n广州, 12℃\n重庆, 8℃\n成都, 12℃"
        temperatures = extract_temperatures_from_text(text)
        assert temperatures == [-4.0, 3.0, 12.0, 8.0, 12.0]

    def test_extract_temperatures_from_text_with_decimal_temperatures(self):
        text = "北京，-4.5℃\n上海, 3.2℃\n广州, 12.7℃\n重庆, 8.9℃"
        temperatures = extract_temperatures_from_text(text)
        assert temperatures == [-4.5, 3.2, 12.7, 8.9]
