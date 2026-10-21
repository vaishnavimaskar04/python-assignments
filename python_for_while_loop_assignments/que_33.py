text = input("Enter a string:")
reverse = ""
i = len(text) - 1

while i >= 0:
    reverse = reverse + text[i]
    i = i - 1

print("Reversed string =", reverse)