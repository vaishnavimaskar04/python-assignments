num = int(input("Enter a number: "))

if -9 <= num <= 9:
    print("Single digit")
elif -99 <= num <= 99:
    print("Double digit")
elif -999 <= num <= 999:
    print("Three digit")
else:
    print("More than three digits")