nterms =int(input())
n1 = 0
n2 = 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   while count < nterms:
       print(n2,end=' ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
