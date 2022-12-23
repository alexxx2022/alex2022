import pytest

from app.calculator import Calculator


class TestCalculator:
    def setup(self):
        self.calculator = Calculator

    def test_adding(self):
        assert self.calculator.adding(self, 1, 1) == 2

    def test_multiply(self):
        assert self.calculator.multiply(self, 2, 3) == 6

    def test_division(self):
        assert self.calculator.division(self, 4, 2) == 2

    def test_subtraction(self):
        assert self.calculator.subtraction(self, 5, 3) ==2

    def teardown_class(self):
        print("Выполнение метода Teardown_class")
