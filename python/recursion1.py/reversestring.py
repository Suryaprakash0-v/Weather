def reverse_string(s):
    def helper(left,right):
        if left>=right:
            return
        s[left],s[right]=s[right],s[left]
        helper(left+1,right-1)#increase the both side of index

    helper(0,len(s)-1)#strat 0 to last index
    return s
print(reverse_string(['s','u','r','y','a']))