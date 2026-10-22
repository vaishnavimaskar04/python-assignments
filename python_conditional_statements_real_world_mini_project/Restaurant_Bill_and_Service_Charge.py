# Restaurant Bill and Service Charge

name = input("Enter customer name: ")
bill = float(input("Enter food bill amount: ₹"))
membership = input("Are you a member? (Yes/No): ")

print("\n----- Restaurant Bill -----")

if bill < 0:
    print("Invalid bill amount")

else:
    # Find discount
    if bill >= 5000:
        discount_percent = 15

    elif bill >= 3000:
        discount_percent = 10

    elif bill >= 1000:
        discount_percent = 5

    else:
        discount_percent = 0

    discount = bill * discount_percent / 100
    amount_after_discount = bill - discount

    # Member discount
    if membership.lower() == "yes":
        member_discount = amount_after_discount * 5 / 100
        discount = discount + member_discount
        amount_after_discount = amount_after_discount - member_discount

    # Service charge after discount
    service_charge = amount_after_discount * 5 / 100
    final_amount = amount_after_discount + service_charge

    print("Customer Name:", name)
    print("Original Bill: ₹", bill)
    print("Discount: ₹", discount)
    print("Service Charge: ₹", service_charge)
    print("Final Payable Amount: ₹", final_amount)

    if final_amount >= 5000:
        print("Message: Thank you for being a valued customer")
