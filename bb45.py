n=int(input())
count=0
while(n%10!=0):
    remainder=n%10
    count=count+1 
    n=n//10
print(count)
