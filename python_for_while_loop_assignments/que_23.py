num = int(input("Enter a number:"))
num = abs(num)
total = 0

while num > 0:
    digit = num % 10

    if digit % 2 != 0:
        total = total + digit

    num = num // 10

print("Sum of odd digits =", total)