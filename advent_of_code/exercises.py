from typing import List

import numpy as np
import pandas as pd

from advent_of_code.get_data import read_file_as_int


def number_of_increases(measurements: List[int]) -> int:
    return sum(np.greater(measurements[1:], measurements[:-1]))


def number_of_increases_sliding_window(measurements: List[int], window_length: int = 3) -> int:
    sliding_window_sum = pd.Series(measurements).rolling(window=window_length).sum()
    return number_of_increases(list(sliding_window_sum.loc[~sliding_window_sum.isna()]))


if __name__ == "__main__":
    day = "one"
    input_data = read_file_as_int(day)
    answer_1 = number_of_increases(input_data)
    print(answer_1)
    answer_2 = number_of_increases_sliding_window(input_data)
    print(answer_2)
