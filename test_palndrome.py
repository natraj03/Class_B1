from sringfunctions import check_palendrome


def test_steingTest():
    assert check_palendrome("madam") == "madam is a palendrome"
    assert check_palendrome("MadaM") == "MadaM is a palendrome"
    assert check_palendrome("Madam") == "Madam is not a palendrome"

def test_numTest():
    assert check_palendrome("989") == "989 is a palendrome"
    assert check_palendrome("999") == "999 is a palendrome"
    assert check_palendrome("998") == "998 is not a palendrome"
