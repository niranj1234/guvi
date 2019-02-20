A=int(input())
B = [int(x) for x in input().split()]
if(A==len(B)):
    for index, value in enumerate(B):
        print(value, index)
