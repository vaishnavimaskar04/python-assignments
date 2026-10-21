age = int(input("Enter age: "))
salary = float(input("Enter salary: "))

if age >= 21:
    if salary >= 25000:
        print("Eligible for loan")
    else:
        print("Not eligible: salary is low")
else:
    print("Not eligible: age is low")