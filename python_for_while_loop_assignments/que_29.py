n = int(input("Enter the number of terms:"))

if n <= 0:
    print("Please enter a positive number.")
else:
    i = 1

    while i <= n:
        print(i, end=" ")
        i = i + 1