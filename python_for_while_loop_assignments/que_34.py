text = input("Enter a string:")
cleaned = text.replace(" ", "").lower()
reverse = ""
i = len(cleaned) - 1

while i >= 0:
    reverse = reverse + cleaned[i]
    i = i - 1

if cleaned == reverse:
    print("Palindrome string")
else:
    print("Not a palindrome string")