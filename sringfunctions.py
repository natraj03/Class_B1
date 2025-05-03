# inputt = "Madam"
# output = "madam" is a palendrome

# iput = "India"
# output = "India" in not a palendrome

# madam
# madam
# India
# aidnI


def check_palendrome(inp1):
    palenOutput = ""
    for char1 in inp1: # India
        # print("char1=",char1)
        # print("palenOutput=",palenOutput)
        palenOutput =  char1 + palenOutput  # I+"", N+I, d+ni current Value + previousvalue
        # palenOutput =    palenOutput + char1# I+"", I+N, In+d previousvalue + current

        # print("after assignment palenOutput=",palenOutput)
#
    if inp1 == palenOutput:
        return inp1 + " is a palendrome"
    else:
        return inp1 + " is not a palendrome"
#
#
#
#
print(check_palendrome("989"))
# temp = "india"
# print(temp[0])
# print(temp[1])
# print(temp[2])
# print(temp[3])
# print(temp[4])
#
# # finalresult = temp[4] + temp[3] + temp[2] + temp[1] + temp[0]
# finalresult = temp[0] + temp[1] + temp[2] + temp[3] + temp[4]

# print(finalresult)
#
# test = "1"
# test2 = "2"
# print("test=",test)
# test = test + test2
# print("test=",test)

