word = input("Please enter in a word: ")
wordLen = len(word)
vowels = ""
for x in range(wordLen):
	letter = word[x]
	if(letter == "a" or letter == "i" or letter == "e" or letter == "o" or letter == "u"):
		vowels += letter
		
		
print("vowels enter:", vowels)
		
