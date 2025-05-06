
def addfun(arg1,arg2):
    return arg1 + arg2


def mulfun(arg1,arg2):
    return arg1 * arg2

def subfun(arg1,arg2):
    return arg1 - arg2



#
# tem1 = 10.1
# tem2 = 100.2
#
# print(addfun(tem1,tem2))
# print(mulfun(tem1,tem2))
# print(subfun(tem1,tem2))



# level 1 no input no output
def tempfunc():
    print("nothing", 5 * 4)

tempfunc()

# level 2 function with input
def leve2fun(arg1):
    print("my input", arg1)


leve2fun(8)
leve2fun("test ing func input")


# func with output without input
def outfunc():
    print("test output only")
    return 5 * 5
test = outfunc()

print(test)

# func with input and output
def outputfunc(tes1,test2,):
    test123 =  tes1 * test2
    print("mulresult", test123)

    def tesmfunc():
        tesm2222 = "test"
        print("tesm2222",tesm2222)
        print("tesmfunc test123",test123)

    tesmfunc()
    return test123




myout = outputfunc(5,4)  # 20

print("myout",myout)
print("adding soemthing", myout + 10)



