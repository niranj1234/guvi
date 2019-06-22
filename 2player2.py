a,b=map(int,input().split())
s1 = [int(x) for x in input().split()]
c=0
while(c<b):
    s1 = [s1[-1]] + s1[:-1]
    c=c+1
print(*s1,sep=' ')
