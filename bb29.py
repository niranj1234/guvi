a=int(input())
c=a%60
d=a/60
e=str(d)
f=e[:e.index('.')]
f=int(f)
if(f<1):
    h=0 
    print(h,c)
else:
    print(f,c)
    
