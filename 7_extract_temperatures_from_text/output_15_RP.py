from typing import List

def extract_temperatures_from_text(text: str) -> List[float]:
    temperatures = []
    lines = text.split('\n')
    for line in lines:
        temp = line.split(', ')[1].replace('℃', '')
        temperatures.append(float(temp))
    return temperatures

def calculate_average_temperature(temperatures: List[float]) -> float:
    return sum(temperatures) / len(temperatures)

def find_highest_temperature(temperatures: List[float]) -> float:
    return max(temperatures)

def find_lowest_temperature(temperatures: List[float]) -> float:
    return min(temperatures)