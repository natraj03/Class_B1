from calculator import mulfun, addfun, tempfunc
import openpyxl
import pytest

# pip install openpyxl
#  run this above command in case you get error: No module named 'openpyxl'

workbook = None


def setup_function():
    global workbook
    workbook = openpyxl.load_workbook("practicefile.xlsx")

    print("\n I am setup function")


def teardown_function():
    global workbook
    if workbook:
        workbook.close()
    print("I am teardown")



@pytest.fixture
def allvalues():
    sheet = workbook.active
    values = []
    for item in sheet.iter_rows(values_only=True):
        values.append(item)
    print("All values", values)
    return  values

def test_add(allvalues):

    firstRow = allvalues[0]  # row 0 first row
    assert addfun(firstRow[0], firstRow[1]) == 15

    twoRow = allvalues[1]  # row 1 or second
    assert addfun(twoRow[0], twoRow[1]) == 35

    threeRow = allvalues[2]  # row 2 or third row
    assert addfun(threeRow[0], threeRow[1]) == 3
    print("add func")


def test_mul():
    assert mulfun(10, 5) == 50
    print("mult func")
