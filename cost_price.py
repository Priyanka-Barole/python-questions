# Que-write a program to accept the cost price of a bike and display the rood thx to be paid according the followig cr
cost_price=int(input("enter the cost price:"))
if cost_price>100000:
	print("Road Tax to be paid",(15/100)*cost_price)
elif cost_price>50000 and cost_price<=100000:
	print("Road Tax to be paid",(10/100)*cost_price)
else:
	print("Road Tax be paid",(5/100)*cost_price)		