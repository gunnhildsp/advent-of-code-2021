import pytest

from advent_of_code.exercises import number_of_increases, number_of_increases_sliding_window


@pytest.fixture()
def day1_example():
    return [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_number_of_increases(day1_example):
    assert number_of_increases(day1_example) == 7


def test_number_of_increases_sliding_window(day1_example):
    assert number_of_increases_sliding_window(day1_example) == 5
