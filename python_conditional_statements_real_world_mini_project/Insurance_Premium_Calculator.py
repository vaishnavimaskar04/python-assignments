# Insurance Premium Calculator

name = input("Enter customer name: ")
age = int(input("Enter age: "))
occupation = input("Enter occupation risk (Low/Medium/High): ")
smoker = input("Are you a smoker? (Yes/No): ")

print("\n----- Insurance Premium -----")

if age < 18:
    print("Customer Name:", name)
    print("Eligibility: Not Eligible")
    print("Reason: Age is below 18")

else:
    base_premium = 10000
    additional_charges = 0

    # Age charge
    if age > 50:
        additional_charges = additional_charges + 5000

    # Occupation risk charge
    if occupation.lower() == "high":
        additional_charges = additional_charges + 7000

    elif occupation.lower() == "medium":
        additional_charges = additional_charges + 3000

    elif occupation.lower() == "low":
        additional_charges = additional_charges + 0

    else:
        print("Invalid occupation risk")

    # Smoker charge
    if smoker.lower() == "yes":
        additional_charges = additional_charges + 5000

    final_premium = base_premium + additional_charges

    print("Customer Name:", name)
    print("Eligibility: Eligible")
    print("Base Premium: ₹", base_premium)
    print("Additional Charges: ₹", additional_charges)
    print("Final Premium: ₹", final_premium)

    if additional_charges >= 10000:
        print("Risk Message: High Risk Policy")
    else:
        print("Risk Message: Normal Risk Policy")