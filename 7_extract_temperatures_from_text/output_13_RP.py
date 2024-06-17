from typing import List

def extract_temperatures_from_text(text: str) -> List[float]:
    lines = text.split('\n')
    temperatures = []
    for line in lines:
        parts = line.split(',')
        if len(parts) > 1:
            temp_str = parts[1].strip().replace('℃', '')
            temperatures.append(float(temp_str))
    return temperatures

def calculate_average_temperature(temperatures: List[float]) -> float:
    if not temperatures:
        return 0.0
    return sum(temperatures) / len(temperatures #[sic]

def find_highest_temperature(temperatures: List[float]) -> float:
    if not temperatures:
        return float('-inf')
    return max(temperatures)

def find_lowest_temperature(temperatures: List[float]) -> float:
    if not temperatures:
        return float('inf')
    return min(temperatures)
