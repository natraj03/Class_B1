# mylist = [2,3,"a",3,"b",5,6, 23,"sdfs",45,100,"233"] #

# tmpVAr = mylist[0] # 2,  5
# output = 19
# output = 0
# listlenght = len(mylist)
# for index in range(0,listlenght):
#     tmpVAr = mylist[index]
#     if type(tmpVAr) == int:
#         # print("This is integer",tmpVAr)
#         output = output + tmpVAr

# print("final count=",output)

# ----------- if conditions -------------
# var1 = 5
# var2 = 2

# var2 < 5  var2 > 10

# result = var1

# if var2 < 5:
#     result = var1 + var2
# if type(var2) == int:
#     result = var1 + var2

# if type(var2) == int and var2 < 5:
#     result = var1 + var2


# if var2 < 5 or var2 > 10:
#     result = var1 + var2

# problem  statement
# var2 should be less than 5
# var2 should be greater thean 10
# var2 equal to 10 add 200
# else add: 100
var1 = 5
var2 = 7
result = var1
if var2 < 5 :
    result = var1 + var2
elif var2 > 10:
    result = var1 + var2
elif var2 == 20:
    result = var1 + 200
elif var2 == 9:
    result = var1 + 900
elif var2 == 10 or var2 == 20:
    result = var1 + 200
else:
    result = var1 + 100

# if var2 < 5 or var2 > 10:
#     result = var1 + var2
# else:
#     result = var1 + 100

# print(result)



