# Loop
# for <variable> in range(start, end-1):
#
#
#

# for i in range(5, 11):
#     print(i * 2)

inpVAr = "News"
outputstr = ""
print("string Length",len(inpVAr))

for index in range(0,len(inpVAr)):
    temp = inpVAr[index]
    outputstr = temp + outputstr
    # outputstr =  outputstr + temp


print("final output",outputstr)





