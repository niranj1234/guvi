i=input()
l=len(i)
count=0
for j in range(0,l):
   if(i[j].isnumeric()):
       count=count+1
print(count)
