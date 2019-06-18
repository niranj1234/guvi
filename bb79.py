a,m=map(int,input().split())
n=a*m 
x = n // 2
y = set([x])
while x * x != n:
    x = (x + (n // x)) // 2
    if x in y:
        print('no')
        break
    y.add(x)
else:
    print('yes')
