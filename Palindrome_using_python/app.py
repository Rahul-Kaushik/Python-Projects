text = input("Type a word or phrase: ")  # e.g. "Madam" or "Was it a car or a cat I saw"

cleaned = text.lower().replace(" ", "")
reversed_text = cleaned[::-1]

print("Cleaned string is:", cleaned)

if cleaned == reversed_text:
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")
