arr=[67,98,46,89,1,465,7070]

first=second=0#get the infinity to the both of thrm

for i in arr:
    if i>first:
        second=first#store the second largest
        first=i#store the first largest
    elif i<first and i!=first:
        second=i
print(second)        

