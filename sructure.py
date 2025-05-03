# import Statements


temp1 = 5
temp2 = 4

def mult():
    xyz = 5
    xyz2 = 4
    global temp2

    print( xyz * xyz2)
    xyz2 = xyz2 + temp2
    temp2 = temp2 + xyz2

    # print(temp1 + temp2)
    print("xyz2 Value=",xyz2)
    print("temp2 Value=",temp2)

def add():
    print(temp1 + temp2)

mult()
add()



