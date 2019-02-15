a=int(input())
numbers=[int(i) for i in input().split()]
c=len(numbers)
if(a==c):
    d=round((c-1)/2)
    b = sorted(numbers)
    e=b[d]
    print(e)
