def natural_numbers(n):
    if n==0: #base
        return  
    natural_numbers(n-1)
    print(n,end=' ')
natural_numbers(10)
