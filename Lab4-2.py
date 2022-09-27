max = float(input("Enter in a number: "))
for x in range(4):
	new = float(input("Enter in another number: "))
	if(new > max):
		max = new
		
print("The largest number entered in was", max)
	
