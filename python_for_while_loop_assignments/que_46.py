num = int(input("Enter a number: "))
n = int(input("Enter the number of multiples: "))

if n <= 0:
    print("Please enter a positive number of multiples.")
else:
    for i in range(1, n + 1):
        print(num, "x", i, "=", num * i)