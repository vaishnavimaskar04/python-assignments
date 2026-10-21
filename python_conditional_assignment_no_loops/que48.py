choice = int(input("Choose language (1-3): "))

match choice:
    case 1:
        print("English")
    case 2:
        print("Hindi")
    case 3:
        print("Marathi")
    case _:
        print("Invalid choice")