word = input("Please enter in a sentance: ")
wordLen = len(word)
count = 0
for x in range(wordLen):
	letter = word[x]
	if(letter == "a"):
		print("There is an \"a\" at:", x)
		count += 1

if(count == 0):
	print("There were no letter \"a's\" in this sentance")
