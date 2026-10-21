choice = int(input("Enter choice (1-4): "))

match choice:
    case 1:
        print("Check Balance")
    case 2:
        print("Deposit Money")
    case 3:
        print("Withdraw Money")
    case 4:
        print("Exit")
    case _:
        print("Invalid choice")