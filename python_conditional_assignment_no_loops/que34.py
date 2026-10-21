year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        print("Leap year and century year")
    else:
        print("Leap year but not a century year")
else:
    print("Not a leap year")