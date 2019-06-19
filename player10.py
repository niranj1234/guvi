i,e=map(str,input().split())
count=0
for j in range(0,len(i)):
  if(i[j]!=e[j]):
    count=count+1
if(count==1):
  print("yes")
else:
  print("no")
