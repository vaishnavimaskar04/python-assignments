# Hotel Room Booking System

name = input("Enter guest name: ")
room_type = input("Enter room type (Standard/Deluxe/Suite): ")
nights = int(input("Enter number of nights: "))

print("\n----- Hotel Booking -----")

if nights <= 0:
    print("Invalid number of nights")
    print("Number of nights must be greater than 0")

elif room_type.lower() == "standard":
    price_per_night = 2000

    room_charge = price_per_night * nights

    if nights >= 10:
        discount_percent = 20
    elif nights >= 5:
        discount_percent = 10
    else:
        discount_percent = 0

    discount = room_charge * discount_percent / 100
    final_amount = room_charge - discount

    print("Guest Name:", name)
    print("Room Type: Standard")
    print("Number of Nights:", nights)
    print("Room Charge: ₹", room_charge)
    print("Discount: ₹", discount)
    print("Final Booking Amount: ₹", final_amount)

elif room_type.lower() == "deluxe":
    price_per_night = 3500

    room_charge = price_per_night * nights

    if nights >= 10:
        discount_percent = 20
    elif nights >= 5:
        discount_percent = 10
    else:
        discount_percent = 0

    discount = room_charge * discount_percent / 100
    final_amount = room_charge - discount

    print("Guest Name:", name)
    print("Room Type: Deluxe")
    print("Number of Nights:", nights)
    print("Room Charge: ₹", room_charge)
    print("Discount: ₹", discount)
    print("Final Booking Amount: ₹", final_amount)

elif room_type.lower() == "suite":
    price_per_night = 6000

    room_charge = price_per_night * nights

    if nights >= 10:
        discount_percent = 20
    elif nights >= 5:
        discount_percent = 10
    else:
        discount_percent = 0

    discount = room_charge * discount_percent / 100
    final_amount = room_charge - discount

    print("Guest Name:", name)
    print("Room Type: Suite")
    print("Number of Nights:", nights)
    print("Room Charge: ₹", room_charge)
    print("Discount: ₹", discount)
    print("Final Booking Amount: ₹", final_amount)

else:
    print("Invalid room type")