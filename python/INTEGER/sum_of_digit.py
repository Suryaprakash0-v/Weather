number=250
sum_digit=0#init the sum 0

while(number>0):#check the condition
    digit=number%10#get the last digit of num
    sum_digit+=digit#sum the digit to sum_digit
    number//=10#remove the last digit
print(sum_digit)

#for loop
num='987978'#the number initial put as a string.the loop iteration don't get the int
sum_digit=0

for i in num:
    sum_digit+=int(i)#convert str into int and sum the sum_dight
print(sum_digit)