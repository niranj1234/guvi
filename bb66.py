X=int(input())
for i in range(2, X):
	if (X%i == 0):
		print("no")
		break
else:
	print("yes")
