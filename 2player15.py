N=input()
b=0
for i in N:
    if N.count(i)>b:
        b=N.count(i)
        c=i
        
print(c)
