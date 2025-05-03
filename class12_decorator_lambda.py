# input1 = 1
# input2 =2
# input3 = 3
# input4 =4
# input5 = 5
# input6 =6
#
# print(input1 + input2 + input3 + input4 + input5 + input6 )
#
# def addusingFunc(inp1,inp2,inp3,inp4,inp5,inp6):
#     print(inp1 + inp2 + inp3 + inp4 + inp5 + inp6)
#
#
# addusingFunc(input1,input2,input3,input4,input5,input6)
#
# addAll = lambda inp1,inp2,inp3,inp4,inp5,inp6: inp1 + inp2 + inp3 + inp4 +inp5 + inp6
#
# print(addAll(input1,input2,input3,input4,input5,input6))


# Decorator:

def validIntOnly(func):
    # print("what is here",func)
    def wrapperFunc(arg1, arg2):
        if type(arg1) == int and type(arg2) == int:
            func(arg1,arg2)
        else:
            print("Please enter valid integers for both input")

    return wrapperFunc

@validIntOnly
def multFunc(inp1,inp2):
    # if type(inp1) == int and type(inp2) == int:
    print("multiplicationn of 2 numbers=", inp1 * inp2)
    # else:
    #     print("Please enter valid integers for both input")


multFunc("123","1234")

@validIntOnly
def addFunc(inp1,inp2):
    # if type(inp1) == int and type(inp2) == int:
    print("Addition of 2 numbers=", inp1+inp2)
    # else:
    #     print("Please enter valid integers for both input")

addFunc(5,9)

@validIntOnly
def subFunc(inp1,inp2):
    print("substraction  of 2 numbers=", inp1 - inp2)

subFunc(5,"123")
















