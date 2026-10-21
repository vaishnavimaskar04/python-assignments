text = input("Enter a string: ")
ch = input("Enter character: ")

first = text.find(ch)
last = text.rfind(ch)

print("First occurrence:", first)
print("Last occurrence:", last)