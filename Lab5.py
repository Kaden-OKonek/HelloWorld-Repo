#Lab 5.1

f = open("readfile.txt", "r")
print(f.read())


#Lab 5.2

f = open("writefile.txt", "w")
f.write("This is a test for lab 5.2")
f = open("writefile.txt", "r")
print(f.read())
f.close()


#Lab 5.3

f2 = open("tempsf.txt", 'w')
with open('temps.txt', 'r') as file:
    for line in file:
        for word in line.split():
            word = float(word)
            word = (word*9/5)+35
            word = str(word)
            f2.write(word)
            f2.write("\r")
f2.close()
f2=open("tempsf.txt", 'r')
print(f2.read())

           
