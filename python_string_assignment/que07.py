text = input("Enter a string: ")
sub = input("Enter substring: ")

if text.endswith(sub):
    print("String ends with the given substring")
else:
    print("String does not end with the given substring")