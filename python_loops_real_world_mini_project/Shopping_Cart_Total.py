# Shopping Cart Total

products = int(input("Enter number of products: "))

subtotal = 0

for i in range(1, products + 1):

    print("\nProduct", i)

    price = float(input("Enter price: ₹"))
    quantity = int(input("Enter quantity: "))

    if price < 0 or quantity < 0:
        print("Invalid price or quantity")
    else:
        item_total = price * quantity
        subtotal = subtotal + item_total

print("\nSubtotal: ₹", subtotal)

# Discount
if subtotal >= 3000:
    discount = subtotal * 10 / 100
else:
    discount = 0

discounted_amount = subtotal - discount

# Delivery
if discounted_amount < 1500:
    delivery_charge = 100
else:
    delivery_charge = 0

final_amount = discounted_amount + delivery_charge

print("Discount: ₹", discount)
print("Delivery Charge: ₹", delivery_charge)
print("Final Payable Amount: ₹", final_amount)