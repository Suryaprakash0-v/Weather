def reversed(s):
    if len(s)==0:
        return''#return the slicing str
    return reversed(s[1:])+s[0]#slicing the first string and store the string in the first index of the string(s[0])
print(reversed(8786))