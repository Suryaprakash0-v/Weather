arr=[1,2,0,0,4,5]
pos=0#pos only change if the value non zero

for i in range(len(arr)):
    if arr[i]!=0:
        arr[pos],arr[i]=arr[i],arr[pos]
        pos+=1
print(arr)