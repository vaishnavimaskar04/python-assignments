# ATM PIN Verification

correct_pin = "1234"

attempts = 0
access_granted = False

while attempts < 3:

    pin = input("Enter your ATM PIN: ")
    attempts = attempts + 1

    if pin == correct_pin:
        print("Access Granted")
        access_granted = True
        break
    else:
        print("Incorrect PIN")
        print("Attempts remaining:", 3 - attempts)

if access_granted == False:
    print("Card Temporarily Locked")

print("Attempts Used:", attempts)