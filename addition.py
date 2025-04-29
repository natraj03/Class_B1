# outputstr = "gnitset"

# firstname = "Rashmi"
# lastname = "Ranjan"
# empyt = " "
# fullname = firstname + empyt + lastname
# print(fullname)
# outputstr = "gnitset"

inpster = "rashmi"
# outputstr = inpster[0] + inpster[1] + inpster[-3] + inpster[-4] + inpster[-5] + inpster[-6] + inpster[-7]

# outputstr = inpster[-1] + inpster[-2] + inpster[-3] + inpster[-4] + inpster[-5] + inpster[-6] + inpster[-7]
outputstr = ""

for index in range(0,len(inpster)):
    outputstr = inpster[index] + outputstr

# outputstr = inpster[0] + outputstr
# outputstr = inpster[1] + outputstr
# outputstr = inpster[2] + outputstr
# outputstr = inpster[3] + outputstr
# outputstr = inpster[4] + outputstr
# outputstr = inpster[5] + outputstr

print(outputstr)
# inpster = "rashmi"

# #Loop 0  r
# output =  inpster[0]
#  print("output",output) # r
#
# #Loop 1 a
# output =   inpster[1] + output
#  print("output",output) # a + r = ar
#
# #Loop 2 s
# output = (inpster[2] + output )
#  print("output",output) # sar


