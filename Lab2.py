"""Lab 2.1:"""

temp1 = eval(input("Please enter in a celsius temputure to be converted: "))
temp2 = ((9/5*temp1)+32)
print(temp1, " degrees is equal to ", temp2, " in fahrenheit")

print("")
"""Lab 2.2"""

num1 = float(input("Please enter in a number: "))
num2 = float(input("Please enter in a second number: "))
sum = num1 + num2
average = sum/2
print("First add the numbers together: ", num1, " + ", num2, "=", sum)
print("Next divid the sum by 2: ", sum, "/2")
print("average = ", average)

print("")

"""Lab 2.3"""

print ('3+4')
print ('The value of 3+4 is', 3+4)
print ('The value of 3+4 is ', 3+4, '.')
print ('The value of 3+4 is ', 3+4, '.', sep= '')
print('On the first line')
print('On the second line')
print ('On the first line', end= ' ')
print ('On the second line')
