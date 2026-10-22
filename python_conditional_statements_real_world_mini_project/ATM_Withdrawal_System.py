# ATM Withdrawal System

name = input("Enter account holder name: ")
balance = float(input("Enter current balance: ₹"))
withdrawal = float(input("Enter withdrawal amount: ₹"))

print("\n----- ATM Transaction -----")
print("Account Holder:", name)

if withdrawal <= 0:
    print("Transaction Status: Rejected")
    print("Reason: Withdrawal amount must be greater than ₹0")

elif withdrawal > balance:
    print("Transaction Status: Rejected")
    print("Reason: Insufficient balance")

elif withdrawal > 20000:
    print("Transaction Status: Rejected")
    print("Reason: Maximum withdrawal allowed is ₹20,000")

else:
    remaining_balance = balance - withdrawal

    print("Transaction Status: Successful")
    print("Withdrawn Amount: ₹", withdrawal)
    print("Remaining Balance: ₹", remaining_balance)

    if remaining_balance < 1000:
        print("Warning: Low Balance Warning")