class MyStringPrograms:
    inpuStr = "malayalam"

    def reverseString(self):
        tempStr = ""
        for char in self.inpuStr:
            tempStr = char + tempStr

        return tempStr

    def checkPalendrome(self, inp1, inp2):
        return inp1 == inp2

    def countChars(self, inp1):
        tempDic = {}
        for char in inp1:
            if char in tempDic:
                tempDic[char] = (tempDic[char] + 1)
            else:
                tempDic[char] = 1
        return tempDic

    def performAllActions(self):
        print("perform all actions")
        revStr = self.reverseString()
        print("is palendrome=",self.checkPalendrome(self.inpuStr, revStr))
        print(self.countChars(self.inpuStr))



myObj = MyStringPrograms()
myObj.performAllActions()
