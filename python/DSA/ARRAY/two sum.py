arr=[1,2,3,4,5,6]
Target=7
left=0
Right=len(arr)-1

while left<Right:
    act=arr[left]+arr[Right]
    if act==7:
        target=act
        print(act)
        break
    elif act<Target:
        left+=1
    elif act>Target:
        right-=1