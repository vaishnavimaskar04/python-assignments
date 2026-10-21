n = int(input("Enter the number of terms:"))

if n <= 0:
    print("Please enter a positive number.")
else:
    i = 1

    while i <= n:
        print(2 * i - 1, end=" ")
        i = i + 1