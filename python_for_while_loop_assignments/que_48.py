num = int(input("Enter a non-negative integer:"))

if num < 0:
    print("Please enter a non-negative integer.")
else:
    original = num
    total = 0

    if num == 0:
        total = 1

    while num > 0:
        digit = num % 10
        fact = 1

        for i in range(1, digit + 1):
            fact = fact * i

        total = total + fact
        num = num // 10

    if total == original:
        print("Strong number")
    else:
        print("Not a strong number")