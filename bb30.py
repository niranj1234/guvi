hr1,min1=map(int,input().split())
hr2,min2=map(int,input().split())
a=hr1*60+min1
b=hr2*60+min2
if(a>b):
    c=a-b
    print(c//60,c%60)
else:
    d=b-a
    print(d//60,d%60)
