# list is Collection
# list mutable // you can add and delete element form list

#  added list of numbers
#  problem statement: [1,4,2,3,7,1,5,2] remove duplicate numbers form list
#  output = [1,4,2,3,7,5]
#
# inputlist = [1,4,2,3,7,1,5,2,4,3]
# outputList = []
# duplicateValues = []
# for item in inputlist:  # 1
#     if item not in outputList:
#         outputList.append(item)
#     else:
#         duplicateValues.append(item)
#
# print(outputList)
# print(duplicateValues)


inputlist = [1,4,2,3,7,11,5,2,4,3]

# maxnumber = inputlist[0]
# if maxnumber < inputlist[1]:
#     maxnumber = inputlist[1]
#
# if maxnumber < inputlist[2]:
#     maxnumber = inputlist[2]
#
# if maxnumber < inputlist[5]:
#     maxnumber = inputlist[5]
#
# if maxnumber < inputlist[7]:
#     maxnumber = inputlist[7]

# maxnumber = inputlist[2]
# print(maxnumber)


#  find the max number from a list
inputlist = [1,4,2,3,7,11,5,2,4,3]
#
# maxNumber = inputlist[0]
#
# for item in inputlist:
#     if maxNumber < item:
#         maxNumber = item
#
# print(maxNumber)
#  find the max number from a list
inputlist = [11,15,12,41,13,0,-1]

minNumber =  inputlist[0]

for item in inputlist:
    if minNumber > item:
        minNumber = item

print(minNumber)





