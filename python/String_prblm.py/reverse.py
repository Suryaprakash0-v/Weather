num=[1,2,3,4,5]

mini=num[0]
max=num[0]
i=1
while(i<=len(num)):
    if i<mini:
        mini=i
    elif i>max:
        max=i
    i+=1    
print(mini)
print(max)            


