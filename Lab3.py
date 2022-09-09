"""Exercise Warmup"""
for x in range(5):
	print("Hello my name is Kade")
	
print(" ")

count = 0
for x in range(3):
	num = float(input("Please enter in a number: "))
	square = num**2
	print("The square of ", num, " is ", square)
	count += 1
if count == 3:
	print("The loop is now done")


print(" ")


for x in range(5):
	countDown = 5
	countDown -= x
	print(countDown, end = ' ')
print("Blast off")

"""Practice 2"""
print(" ")

for x in range(4):
	for y in range(6):
		print("*", end = '')
	print(" ")

print(" ")

for x in range(4):
	print('*' * (x+1))


"""Practice 3"""
print(" ")

import random

a = int(input("Enter in a smaller number: "))
b = int(input("Enter in a larger number: "))
randInt = random.randint(a, b)
while True:
    count += 1
    guess = int(input("Enter guess: "))
    if guess < randInt:
        print("Higher")
    elif guess > randInt:
        print("Lower")
    else:
        print("Correct, the number was ", randInt)
        break
