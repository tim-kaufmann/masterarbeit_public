import pytest

import pandas as pd
from io import StringIO
from output_9_CoT import calculate_date_difference

class Testcalculate_date_difference:
    def test_calculate_date_difference_2(self):
        csv_contents = "Date\n2020-01-01\n2020-01-01\n2020-01-01"
        assert calculate_date_difference(csv_contents) == 0

    def test_calculate_date_difference_3(self):
        csv_contents = "Date\n2020-01-01\n2020-12-31"
        assert calculate_date_difference(csv_contents) == 365

    def test_calculate_date_difference_4(self):
        csv_contents = "Date\n2020-01-01\n2021-01-01"
        assert calculate_date_difference(csv_contents) == 366

    def test_calculate_date_difference_5(self):
        csv_contents = "Date,Value\n" \
                       "2024-01-01,100\n" \
                       "2024-02-15,110\n" \
                       "2024-03-10,120\n"

        assert calculate_date_difference(csv_contents) == 69

    def test_calculate_date_difference_6(self):
        csv_contents = "Date,date,DATE\n" \
                       "2020-01-01,100,2020-01-01\n" \
                       "2020-02-15,110,2020-01-02\n" \
                       "2020-03-10,120,2020-01-02\n"
        assert calculate_date_difference(csv_contents) == 69

    def test_calculate_date_difference_7(self):
        csv_contents = "Date\n2020-01-01"
        assert calculate_date_difference(csv_contents) == 0

    def test_calculate_date_difference_8(self):
        csv_contents = "Date\n2020-01-01\n2020-01-01"
        assert calculate_date_difference(csv_contents) == 0

    def test_calculate_date_difference_9(self):
        csv_contents = "Date\n2020-01-01\n2021-01-02\n2022-01-03\n2023-01-04\n2024-01-05\n2025-01-06"
        assert calculate_date_difference(csv_contents) == 1832

    def test_calculate_date_difference_10(self):
        csv_contents = "Date\n2020-01-01\n2022-01-02\n2022-01-03\n2023-01-04\n2023-01-05\n2021-01-06\n2021-01-07"
        assert calculate_date_difference(csv_contents) == 1100