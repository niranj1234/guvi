N,K=map(int,input().split())
n=list(map(int,input().split()))
if(N==len(n)):
    if K in n:
        print('yes')
    else:
        print('no')
