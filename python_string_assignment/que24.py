text = input("Enter a string: ")
result = ""

for ch in text:
    if ch.isdigit():
        result += ch

print("Digits:", result)