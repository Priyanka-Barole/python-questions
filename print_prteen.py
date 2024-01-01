# que-write a program print following pateern.
n=int(input("enter n:"))
lst="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(1,n+1):
	for j in range(i):
		print(lst[j],end="")
	print()	


# que-write a program print following pateern.
n=65
for i in range(1,6):
	for j in range(1,i+1):
		print(chr(n),end="")
		n=n+1
	print()
	
	