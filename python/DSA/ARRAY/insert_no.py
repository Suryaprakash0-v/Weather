arr=[3,5,6,7]
new_element=int(input())
position=int(input())

new_list=[]#create a new list to add the new element

for i in range(len(arr)+1):#get the extra space for add the element range(5)
    if i==position:
        new_list.append(new_element)#add the new element
    if i<len(arr):
        new_list.append(arr[i])#add the existing element

print(new_list)    


