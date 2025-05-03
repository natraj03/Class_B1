# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# range start, end, increment/decremt(stepper) , 2

templist = [11, 5, 3, 4, 10, 1]
# templist3 = [111,5,3,4,10,1]
# templist4 = [101,5,3,4,10,1]


# firstitem = templist[0]

# tempList2 = [templist,templist3,templist4]
tempList2 = [templist]

# firstitem = tempList2[0]  #[11,5,3,4,10,1]
temp = 0

for i in range(0, len(tempList2)):
    tempvarList = tempList2[i]
    for j in tempvarList:
        if temp <= j:
            temp = j
    # if temp <= tempList2[i]: # 0 <= [11,5,3,4,10,1]
    #     temp = tempList2[i]

# for i in templist:
#     if temp <= i:
#         temp = i

print(temp)
