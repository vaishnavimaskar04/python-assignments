n = int(input("Enter a positive integer:"))

if n <= 0:
    print("Please enter a positive integer.")
else:
    total = 0

    for i in range(1, n + 1):
        total = total + i * i

    print("Sum of squares =", total)