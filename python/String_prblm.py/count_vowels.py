#for loop
String='suryaprakash'
vowels='aeioue'
vowels_count=0#vowels starting count
constant_count=0#constant starting count


for i in String:
    if i in vowels:
        vowels_count+=1#the condition true increase the one value
    else:
        constant_count+=1#the condtion false increase the constant count
print(vowels_count)
print(constant_count)
#while loop

String='Veerasamy'
vowels='aeioue'
vowels_count=0#vowels starting count
constant_count=0#constant starting count
i=0

while(i<len(String)):
    ch=String[i]
    if ch in vowels:
        vowels_count+=1
    else:
        constant_count+=1
    i+=1

print(vowels_count)
print(constant_count)    