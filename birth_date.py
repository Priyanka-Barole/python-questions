#write a python prigram chek to team members birthday date. 

Birth_date=int(input("Enter Birthday: "))
i=1
while i<=31:
	i+=1
	if i==Birth_date:
		print("Day{}:team members Birthday.".format(i))
	else:
		print("Day{}:normal day".format(i))

		
Birth_date=int(input("enter Birthday:"))
for i in range(1,32):
	if i==Birth_date:
		print("Day{}:team members Birthday.".format(i))
	else:
		print("Day{}:normal day".format(i))




