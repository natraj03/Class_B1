#  create empty list
# tempList = []
#
# print("tempList",tempList)

# create list with items / objects
# tempLsit = ["a",2,"abc",343,"audfd"]
# print("tempLsit",tempLsit)

# add elements in list
# temp1 = 5
# temp5 = 10
# tem7 = "abcd"
#
# tempLsit = ["a",2,"abc",343,"audfd",temp1,tem7]
#
# print(" tempLsit",tempLsit)
#
# temp6 = tempLsit[3] + temp5
# # add element in the end of the existing list
# tempLsit.append(temp6)
# print(" apter append tempLsit",tempLsit)
# # remove item using item object / int / string
# tempLsit.remove("audfd")
# print(" remove",tempLsit)
# # remove item using index
# tempLsit.pop(2)
# print(" pop using index",tempLsit)
#
# # replace item at index
# tempLsit[0] = 34565
# print("replace item at index",tempLsit)
#
# tempLsit[0] = temp5
# print("replace item at index using variable",tempLsit)

# ----------- List:[] = allows mutability(add,delete) and duplicates and allows index----------
# ----------- set: {} = allows mutability(add,delete) and does not allow duplicates and does not allow index ----------
# ----------- tuple: () = Does not allow mutability(add,delete) and does allow duplicates and allow index----------

mylist = [1,4,6,23,4,5,6,8,3,2]
print(mylist[4])

myset = {1,4,6,23,4,5,6,8,3,2}
print(myset)

# convert set to list/
convertedList = list(myset)
print("tempList",convertedList[4])
# add elements in set
myset.add("mvalue")
myset.add("test")
myset.add("123_test")

print(myset)

# remove elements from set randomly
myset.pop()
print("random pop",myset)
# remove specific elements from set
myset.remove("123_test")
print("delete specific item",myset)

# ========== Tuple ==========
mytuple = (1,4,"a","abc",3,3,1)
print("my tuple",mytuple)

print("my tuple",mytuple[3])
# mytuple.add("123_test")
# mytuple.append("temp6")
print("my tuple",mytuple[3])



