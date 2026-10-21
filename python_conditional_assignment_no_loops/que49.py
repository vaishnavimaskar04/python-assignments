status = input("Enter result status: ").lower()

match status:
    case "pass":
        print("Congratulations! You passed.")
    case "fail":
        print("You failed.")
    case "distinction":
        print("Congratulations! You got distinction.")
    case _:
        print("Invalid status")