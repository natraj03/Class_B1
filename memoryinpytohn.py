#
# a = 5
# b = 10
#
# print("a value", a, "Memory address of a",id(a))
# print("b value", b, "Memory address of b",id(b))
# a = 7
# b = a
# c = b
# d = c
# # 4329210224
# memory_porinter_Reference_Count = [a,b,c]
#
# print("a value", a, "Memory address of a",id(a))
# print("b value", b, "Memory address of b",id(b))
# print("c value", c, "Memory address of b",id(c))
# memory_porinter_Reference_Count = [a,b] = 2
#
#
# print("a value", a, "Memory address of a",id(a))
# print("b value", b, "Memory address of b",id(b))
# memory_porinter_Reference_Count = [] = 1

def myfunc():
    a1 = 1
    print("a1 value",a1)

myfunc()
#
# f = a
# print(a)
# memory_porinter_Reference_Count = [] = 1
# print(f)
#

#
list1 = [1,2,3,4,5,6,[12345]]
myList =  [1,2,3,4,5,"adfaf asdf",[]]
myList3 = [1,2,3,4,5,"adfaf asdf "]

print("list", myList, "Memory address of List",id(myList))
myList.append(9)
print("list", myList, "Memory address of List after change",id(myList))
myList2 = myList
myList2.append(12)
print("myList2", myList2, "Memory address of List after change myList2",id(myList2))
print("myList3", myList3, "Memory address of List after change myList3",id(myList3))
myList3.append(13)

a = 5
b = 5
a = 6
b = 7
print(id(a),id(b))



