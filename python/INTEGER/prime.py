num=int(input(''))
count=0

for i in range(1,num):
    if num%10==0:
        count=count+1
if count == 0:
        print('its prime')
else:
        print('not a prime')