S=input()
d=0
for i in S:
  if((i=='0') or (i=='1')):
    d=d+1
if (d==len(numb)):
  print("yes")
else:
  print("no")
