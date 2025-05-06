def highest_value(d):
    h=0
    for i,j in d.items():
        if h<=j:
            h=j
    return h
d={'a':6,'b':2,'c':8,'d':4}
print(highest_value(d))
