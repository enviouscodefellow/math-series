import pytest
from math_series.math_series import fibonacci


def test_fibonacci_exists():
    assert fibonacci


def test_fibonacci_0():
    actual = fibonacci(0, "n")
    expected = 0
    assert actual == expected


def test_fibonacci_1():
    actual = fibonacci(1, "n")
    expected = 1
    assert actual == expected


def test_fibonacci_2():
    actual = fibonacci(2, "n")
    expected = 1
    assert actual == expected


def test_fibonacci_3():
    actual = fibonacci(3, "n")
    expected = 2
    assert actual == expected


def test_fibonacci_4():
    actual = fibonacci(4, "n")
    expected = 3
    assert actual == expected


def test_fibonacci_5():
    actual = fibonacci(5, "n")
    expected = 5
    assert actual == expected


def test_fibonacci_6():
    actual = fibonacci(6, "n")
    expected = 8
    assert actual == expected