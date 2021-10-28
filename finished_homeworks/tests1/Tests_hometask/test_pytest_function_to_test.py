from Tests_hometask.functions_to_test import *
import pytest


def test_add():
    assert Calculator.add(5, 7) == 12


def test_subtract():
    assert Calculator.subtract(4, 1) == 3


class TestDivide:
    @pytest.mark.parametrize("x, y, expected_value", [(10, 2, 5),
                                                      (30, -2, -15),
                                                      (-150, -50, 3)])
    def test_divide_values(self, x, y, expected_value):
        assert Calculator.divide(x, y) == expected_value

    @pytest.mark.parametrize("exception, x, y", [(ValueError, 150, 0),
                                                 (TypeError, 15, "2")])
    def test_divide_exceptions(self, exception, x, y):
        with pytest.raises(expected_exception=exception):
            Calculator.divide(x, y)

    def test_divide_raises(self):
        with pytest.raises(ValueError):
            Calculator.divide(5, 0)
            Calculator.divide(-3, 0)
            Calculator.divide(122, 0)
            Calculator.divide(-12789, 0)
            Calculator.divide(78913, 0)


def test_multiply():
    assert Calculator.multiply(5, 10) == 50
