from calculatorB2 import *


def test_liistadding():
    assert addListofIntegers([1,2,3]) == 6
    assert addListofIntegers([1, 2, -3]) == 1
    assert addListofIntegers([-1, -2, -3]) == -6

# def test_positive():
#     assert addListofIntegers([1, 2, 3]) == 6
#
# def test_zero():
#     assert addListofIntegers([1, 2, -3]) == 1
#
# def test_negative():
#     assert addListofIntegers([-1, -2, -3]) == -6
