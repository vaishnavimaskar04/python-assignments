while True:
    print("\n--- MENU ---")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Sum =", a + b)

    elif choice == "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Difference =", a - b)

    elif choice == "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Product =", a * b)

    elif choice == "4":
        print("Thank you! Exiting program.")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")