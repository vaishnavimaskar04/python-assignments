num = int(input("Enter a non-negative integer:"))

if num < 0:
    print("Please enter a non-negative integer.")
else:
    original = num
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == original:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")