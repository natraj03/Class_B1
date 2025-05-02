from class_clculator import inpStr, reverseAstring, PalendromeClass, countCharacterrRepeat


class allinOne:

    def doAllprogramsTogather(self):
        reverseObj = reverseAstring()
        reverseStr = reverseObj.revereTheStr(inpStr)
        print("revere of a string=", reverseStr)
        palenObj = PalendromeClass()
        isPalendrome = palenObj.checkPalendrome(inpStr, reverseStr)

        print("given string is palendrome = ", isPalendrome)
        countCharObj = countCharacterrRepeat()
        print(countCharObj.countChars(inpStr))

allinOneOBJ = allinOne()
allinOneOBJ.doAllprogramsTogather()