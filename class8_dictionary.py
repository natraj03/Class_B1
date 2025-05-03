# tempstr = "testing"
# print(tempstr[2])
#
# list1 = ["adf as", 13, 2] # list
# print(list1[1])
#
# mytuple = ("adf as", 13, 2) # tuple
# print(mytuple[1])
#
# myset = {1, 4, 5}
# print(myset)


# myDictonary = {"mykey":"myval", "test1":"123", "test3":"abcd"}
# print(myDictonary["test1"])
#
# name = "srikant"
# age = 24
# address = "local "
# phone = "1234"
#
# mybiodatta = {"name": "Srikanth", "age":24, "address":"local, locaal ", "name1":"rashmi", "phone" : "1234"}
# mybiodatta2 = {"name": "rashmi", "age":25, "address":"local, locaal ", "name1":"rashmi", "phone" : "1234"}
# mybiodatta3 = {"name": "sandip", "age":22, "address":"local, locaal ", "name1":"rashmi", "phone" : "1234"}
mybiodatta4 = {"name": "chandan", "age":29, "address":"local, locaal ", "name1":"rashmi", "phone" : "1234"}
#
#
# print(mybiodatta["address"])
# print(mybiodatta2["phone"])


mybiodatta4["newkey"] = "tseting"
mybiodatta4["name"] = "Chandan kumar"
print(mybiodatta4)

#  find the higest number in dictionary
# a = 10
# b = 15

# c = 20
# dvar = 25
#
# tempList = [10,15,c,dvar]
# finalAdd = tempList[0] + tempList[1] + tempList[2] + tempList[3]
# # print(finalAdd)
#
# inpdict = { "a":10, "b":15, "c":c, "d":dvar}
#
# resultval = inpdict["a"] + inpdict["b"] + inpdict["c"] + inpdict["d"]
#
# # print("final addition",resultval)
#
# # add list of integers using for
# finalval = 0
#
# # style 1
# for index in range(len(tempList)):
#     finalval = finalval + tempList[index]
#
# # style 2
# for item in tempList:
#     finalval = finalval + item
#
#
#
# print("for loop list addition",finalval)
#
# finaldictVal = 0
# # style 1
# for item in inpdict:
#     finaldictVal = finaldictVal + inpdict[item]
#
# # style 2
# # for key1, val1 in inpdict.items():
# #     finaldictVal = finaldictVal + val1
#
#
# print("for loop dictionary addition",finaldictVal)
#
# # inputStr = "india" find which character repeting how many times in a string
# #  output = i:2, n:1, d:1, a:1
#
# inputStr = "subhashree"
#
# outpDict = {}
#
# for char in inputStr:
#
#     if char in outpDict:
#         outpDict[char] = outpDict[char] + 1
#     else :
#         outpDict[char] = 1
#
# print("outpDict",outpDict)