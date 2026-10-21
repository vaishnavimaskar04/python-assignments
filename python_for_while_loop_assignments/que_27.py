num = int(input("Enter a positive integer:"))

if num <= 0:
    print("Please enter a positive integer.")
else:
    print("Factors of", num, "are:")

    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")