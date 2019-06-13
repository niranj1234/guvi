import re
S=input()
if((bool(re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', S)))):
    print("Yes")
else:
  print("No")
