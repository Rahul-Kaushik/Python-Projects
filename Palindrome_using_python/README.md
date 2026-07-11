Project:
Check whether a word or phrase reads the same forwards and backwards

Important Points Observed :
1- [::-1] reverses a string using slicing (start, stop, step of -1)
2- .replace(" ", "") strips spaces so phrases like "a car or a cat" can be checked, not just single words
3- .lower() is needed before comparing, otherwise "Madam" != "madam" case would break the match

input()
✅ slicing [::-1]
✅ .replace()
✅ .lower()
✅ if/else
✅ string comparison
