attendance = float(input("Enter attendance percentage: "))
marks = int(input("Enter marks: "))

if attendance >= 75:
    if marks >= 40:
        print("Eligible for exam")
    else:
        print("Not eligible: marks are low")
else:
    print("Not eligible: attendance is low")