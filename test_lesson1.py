import pytest

from Lesson1 import multFun, addfun, div

def test_mult_positive():
    assert multFun(5,5) == 25

def test_div():
    assert div(4,2) == 2

@pytest.mark.divtest
def test_div2():
    assert div(4,2) == 2
    assert div(6,2) == 3
    assert div(10,2) == 5.0


