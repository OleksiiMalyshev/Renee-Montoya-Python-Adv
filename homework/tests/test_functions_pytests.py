import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator().add(2, 3) == 5

def test_substract():
    assert Calculator().subtract(10,5) == 5

def test_multiply():
    assert Calculator().multiply(2, 2) == 4

def test_division():
    assert Calculator().divide(10, 2) == 5

def test_zero_div():
    with pytest.raises(ValueError):
        Calculator().divide(5, 0)
