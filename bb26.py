a=int(input())
numbers=[int(i) for i in input().split()]
if(a==len(numbers)):
    print(*sorted(numbers))
