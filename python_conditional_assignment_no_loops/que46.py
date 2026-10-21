grade = input("Enter grade (A/B/C/Fail): ").upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "FAIL":
        print("Needs Improvement")
    case _:
        print("Invalid grade")