i=input()
l=len(i)
count=0
for j in range(0,l):
   if(i[j].isnumeric()):
       print("")
       
   elif(i[j].isalpha()):
       print("")
       
   else:
       count=count+1
print(count)
