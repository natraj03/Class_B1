from class1_B2 import mult


def test_positive():
    assert mult(5,10) == 51

def test_1Negative():
    assert mult(5,-10) == -50

def test_2negative():
    assert mult(-5,-10) == -50