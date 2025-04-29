import pytest

from Lesson1 import multFun, addfun, div

@pytest.mark.positive
def test_mult_positive():
    assert multFun(5,5) == 25

@pytest.mark.positive
def test_div():
    assert div(4,2) == 2

@pytest.mark.negative
def test_negative_mult():
    assert multFun(-5,5) == -25