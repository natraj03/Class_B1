#
# myVar = 50
# def printHello():
#     tempvar = myVar * 2
#     print("hello welcome to function tempvarresult =",tempvar)
#
#
# printHello()
# print(myVar)
#
#
# class myfirstClass:
#
#     inpVar = 20
#
#     def addFunc(self):
#         print(self.inpVar  + 10)
#
#
#
# class mysecondClass:
#     inputstr = "hello this second class"
#
#     def myStrFunc(self):
#         print(self.inputstr)
#
#
#
#
# myobj1 = myfirstClass()
# myobj1.addFunc()
#
# myobj2 = mysecondClass()
# myobj2.myStrFunc()
#

# reverse of a string
# find a string is palendrome or not
# count all the repetition of characters in the palendrome

inpStr = "malayalam"


class reverseAstring:

    def revereTheStr(self, inpstring):
        tempStr = ""
        for char in inpstring:
            tempStr = char + tempStr

        return  tempStr


# reverseObj = reverseAstring()
# reverseStr =  reverseObj.revereTheStr(inpStr)
# print("revere of a string=",reverseStr)

class PalendromeClass:

    def checkPalendrome(self, inp1, inp2):
        return inp1 == inp2



# palenObj = PalendromeClass()
# isPalendrome = palenObj.checkPalendrome(inpStr, reverseStr)
#
# print("given string is palendrome = ",isPalendrome)

class countCharacterrRepeat:

    def countChars(self, inp1):
        tempDic = {}
        for char in inp1:
            if char in tempDic:
                tempDic[char] = (tempDic[char] + 1)
            else:
                tempDic[char] =  1
        return  tempDic


# countCharObj =countCharacterrRepeat()
#
# print(countCharObj.countChars(inpStr))





