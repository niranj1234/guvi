i=input()
if len(i)%2!=0:
    s=int(len(i)/2)
    s1=i[:s]
    s2=i[s+1:len(i)]
    print(s1+'*'+s2)
else:
    s=int(len(i)/2)
    s1=i[:s-1]
    s2=i[s+1:len(i)]
    print(s1+'**'+s2)
