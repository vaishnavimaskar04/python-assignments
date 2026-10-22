# Mobile Data Plan Bill

name = input("Enter customer name: ")
plan = input("Enter plan type (Basic/Standard/Premium): ")
extra_data = float(input("Enter extra data used in GB: "))

print("\n----- Mobile Data Bill -----")

if extra_data < 0:
    print("Invalid data usage")
    print("Extra data cannot be negative")

elif plan.lower() == "basic":
    base_charge = 299
    extra_charge = extra_data * 20

    if extra_data > 10:
        surcharge = 100
    else:
        surcharge = 0

    final_bill = base_charge + extra_charge + surcharge

    print("Customer Name:", name)
    print("Plan Type: Basic")
    print("Base Plan Charge: ₹", base_charge)
    print("Extra Data Charge: ₹", extra_charge)
    print("Surcharge: ₹", surcharge)
    print("Final Bill: ₹", final_bill)

elif plan.lower() == "standard":
    base_charge = 499
    extra_charge = extra_data * 20

    if extra_data > 10:
        surcharge = 100
    else:
        surcharge = 0

    final_bill = base_charge + extra_charge + surcharge

    print("Customer Name:", name)
    print("Plan Type: Standard")
    print("Base Plan Charge: ₹", base_charge)
    print("Extra Data Charge: ₹", extra_charge)
    print("Surcharge: ₹", surcharge)
    print("Final Bill: ₹", final_bill)

elif plan.lower() == "premium":
    base_charge = 799
    extra_charge = extra_data * 20

    if extra_data > 10:
        surcharge = 100
    else:
        surcharge = 0

    final_bill = base_charge + extra_charge + surcharge

    print("Customer Name:", name)
    print("Plan Type: Premium")
    print("Base Plan Charge: ₹", base_charge)
    print("Extra Data Charge: ₹", extra_charge)
    print("Surcharge: ₹", surcharge)
    print("Final Bill: ₹", final_bill)

else:
    print("Invalid plan type")