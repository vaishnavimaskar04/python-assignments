num = int(input("Enter a number:"))

if num < 0:
    print("Not a palindrome")
else:
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        print("Palindrome number")
    else:
        print("Not a palindrome")