p,r=map(int,input().split())
k=0
for a in range(p,r+1):
    for i in range(2,a):
        if(a%i==0):
            break
    else:
        k=k+1
print(k)
