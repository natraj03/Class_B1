#
# #  count list of the integers
# # input: [1,4,2,1,3] : 11
# # input: [2,6,7,4,1] : 20
#
# inpList = [1,4,2,1,3]
# outPut = inpList[0] + inpList[1] + inpList[2] + inpList[3] + inpList[4]
# print("List of integer result=",outPut)
#
# output2 = 0
#
#
# print(inpList[2])
#
# # for index in range(0, 10, 1):
# #     print("index value",index)
# #
# # for index in range(5, 10, 1):
# #     print("index value starting from 5",index)
# #
# # for index in range(0, 10, 2):
# #     print("with stepper 2",index)
# #
# # for index in range(0, 10, 3):
# #     print("with stepper 3",index)
# #
# for index in range(len(inpList)):
#     print("range default",index)
#     output2 += inpList[index]
#
# # for obj in inpList:
# #     output2 += obj
#
# print(output2)
#
# # for item in inpList:
#
# print("using sum:",sum(inpList))

def addListofIntegers(inputList):
    output2 = 0
    for item in inputList:
        output2 = output2 + item
    return  output2

print("sum of int List=",addListofIntegers([1,2,3,4,5,6,7]))
















