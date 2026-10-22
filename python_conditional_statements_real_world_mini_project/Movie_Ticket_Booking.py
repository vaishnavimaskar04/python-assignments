# Movie Ticket Booking

name = input("Enter customer name: ")
age = int(input("Enter age: "))
show_type = input("Enter show type (Morning/Evening): ")
day_type = input("Enter day type (Weekday/Weekend): ")

print("\n----- Movie Ticket -----")

if age < 0:
    print("Invalid age")

else:
    original_price = 200
    discount = 0
    weekend_surcharge = 0

    if age < 12:
        discount = original_price * 50 / 100

    elif age >= 60:
        discount = original_price * 30 / 100

    if show_type.lower() == "morning":
        discount = discount + 30

    if day_type.lower() == "weekend":
        weekend_surcharge = 50

    final_price = original_price - discount + weekend_surcharge

    print("Customer Name:", name)
    print("Original Ticket Price: ₹", original_price)
    print("Discount: ₹", discount)
    print("Weekend Surcharge: ₹", weekend_surcharge)
    print("Final Ticket Price: ₹", final_price)