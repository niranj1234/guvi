A=int(input())
numbers=[int(i) for i in input().split()]
C=len(numbers)
if(A==C):
    D=round((C-1)/2)
    B = sorted(numbers)
    E=B[D]
    print(E)
