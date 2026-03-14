text=input("Type the word: ") #Indian Space Research Organisation
print("Entered string is :\n", text)
words =text.split()
#print("Split string is:", words)

abbreviation = ""
for word in words:
    abbreviation = abbreviation + word[0]

print("Abbreviated Form:",abbreviation.upper())