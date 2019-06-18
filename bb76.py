i=int(input())
if i>1:
    for ak in range(2,i):
        if(i%ak==0):
            print('yes')
            break
    else:
        print('no')
else:
    print('yes')
