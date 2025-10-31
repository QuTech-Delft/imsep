from math_utils import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(0, 1) == -1

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(-6, 2) == -3