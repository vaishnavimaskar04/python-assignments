text = input("Enter a sentence:").strip()

if text == "":
    count = 0
else:
    words = text.split()
    count = len(words)

print("Total words =", count)