A,B=map(int,input().split())
for i in range(A+1,B):
    if(i%2==0):
        print(i,end=" ")
    elif(i%2==0 and i==m-1):
        print(i)
        
