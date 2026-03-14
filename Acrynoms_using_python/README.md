Project:
Generate the short form of a word provided in the input

Important Points Observed :
1- append() only works for lists not on strings as strings are immutable(not modified), lists are mutable
2-Variable Naming (PEP 8 Practice) if the list returns multiple words then write words (plural)
3- check this code:

text = "Machine Learning Artificial Intelligence"
words = text.split()

print(words[1][0]) --> this will print L
words[1][0]
│        │
│        └─ first character of the word
└───── second word in the list

input()
✅ split()
✅ for loops
✅ string indexing [0]
✅ string concatenation
✅ .upper()
✅ difference between list vs string