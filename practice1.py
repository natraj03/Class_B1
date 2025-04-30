
#  interchange values of 2 variables without using 3rd variable
# 2, 4 ,
# Expected output : a= 4 b = 2
# a = 2
# b = 4
# output
# a = 4
# b = 2

a = 5
b = 7
print("Initial a value =", a)
print("Initial b value =", b)

a = b + a # a = 12
b = a - b # b = 5
a = a - b  # a = 7

# a, b = b, a

print("Final a value =", a)
print("Final b value =", b)