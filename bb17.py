a=int(input())
sum=0
x=a 
while(x>0):
    y=x%10
    sum+=y**3
    x//=10
   # print(x)
if(a==sum):
    print('yes')
else:
    print('no')
