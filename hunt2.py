x = int(input())
a=[int(i) for i in input().split()]
if(x==len(a)):
    for j in sorted(a, key=int, reverse=True):
        print(j, end="")
        
