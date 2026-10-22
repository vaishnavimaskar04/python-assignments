# Online Shopping Checkout

name = input("Enter customer name: ")
purchase = float(input("Enter purchase amount: "))
customer_type = input("Enter customer type (Regular/Premium): ")

if purchase < 0:
    print("Invalid purchase amount")
else:
    # Find discount
    if purchase >= 5000:
        discount_percent = 20
    elif purchase >= 3000:
        discount_percent = 10
    elif purchase >= 1000:
        discount_percent = 5
    else:
        discount_percent = 0

    discount = purchase * discount_percent / 100
    amount = purchase - discount

    # Premium customer discount
    if customer_type.lower() == "premium":
        premium_discount = amount * 5 / 100
        discount = discount + premium_discount
        amount = amount - premium_discount
    elif customer_type.lower() == "regular":
        pass
    else:
        print("Invalid customer type")
        amount = purchase

    # Delivery charge
    if amount >= 2000:
        delivery_charge = 0
    else:
        delivery_charge = 100

    final_amount = amount + delivery_charge

    print("\n----- Shopping Bill -----")
    print("Customer Name:", name)
    print("Discount Amount: ₹", discount)
    print("Delivery Charge: ₹", delivery_charge)
    print("Final Payable Amount: ₹", final_amount)