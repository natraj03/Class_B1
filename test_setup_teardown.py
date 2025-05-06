from calculator import mulfun,addfun, tempfunc
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




def test_add():
    sheet = workbook.active
    values = []
    for row in sheet.iter_rows(values_only=True):
        values.append(row)
    print("All values",values) # list of touples: [(5.0, 10.0), (15.0, 20.0), (1.0, 2.0), (7.0, 8.0), (12.0, 12.0)]

    firstRow = values[0] # row 0 first row
    assert addfun(firstRow[0],firstRow[1]) == 15

    twoRow = values[1]  # row 1 or second
    assert addfun(twoRow[0], twoRow[1]) == 35

    threeRow = values[2]  # row 2 or third row
    assert addfun(threeRow[0], threeRow[1]) == 3
    print("add func")

def test_mul():
    assert  mulfun(5,10) == 50
    print("mult func")
