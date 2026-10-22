# Multiplication Table and Number Analyzer

number = int(input("Enter a positive integer for table: "))

if number <= 0:
    print("Invalid number")
    print("Please enter a positive integer")

else:

    print("\n----- Multiplication Table -----")

    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

    start = int(input("\nEnter start of range: "))
    end = int(input("Enter end of range: "))

    if start > end:
        print("Invalid range")
        print("Start cannot be greater than end")

    else:
        even_count = 0
        odd_count = 0
        total_sum = 0

        for i in range(start, end + 1):

            total_sum = total_sum + i

            if i % 2 == 0:
                even_count = even_count + 1
            else:
                odd_count = odd_count + 1

        print("\n----- Number Analysis -----")
        print("Start:", start)
        print("End:", end)
        print("Even Count:", even_count)
        print("Odd Count:", odd_count)
        print("Sum of Range:", total_sum)