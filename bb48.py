x=int(input())
y=[int(i) for i in input().split()]
if(x==len(y)):
    a=sum(y)/x   
    b=round(a)
    print(b)
