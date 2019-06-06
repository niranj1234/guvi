N=int(input())
p=0
while(N!=0):
    r=N%10
    p=p+r
    N=N//10
#    print(N)
print(p)
