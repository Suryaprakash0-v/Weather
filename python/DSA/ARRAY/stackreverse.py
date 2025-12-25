def reversedString(s):
    stack=list(s)
    reversed_string=''
    for s in range(0,len(stack)-1):
        reversed_string+=stack.pop()
        return reversed_string
    s-=1
print(reversedString('suryaprakash'))