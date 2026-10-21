num = int(input("Enter a non-negative integer:"))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    print("Factorial =", fact)