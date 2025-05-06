from calculator import mulfun,addfun, tempfunc

def test_add():
    assert addfun(10,10) == 20
    assert addfun(10, 9) == 19
    assert addfun(10.5, 10) == 20.5
    assert tempfunc() == None

def test_mul():
    assert mulfun(10,10) == 101
    assert mulfun(10, 9) == 91
    assert mulfun(10.5, 10) == 106.0


