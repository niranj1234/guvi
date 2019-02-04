a,b=map(str,input().split())
c=[]
d=[]
for i in range(0,len(a)):
    m=a.count(a[i])
    n=b.count(b[i])
    c.append(m)
    d.append(n)
if(c==d):
    print("yes")
else:
    print("no")
