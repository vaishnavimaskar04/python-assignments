# Bank Transaction History

balance = float(input("Enter opening balance: ₹"))
transactions = int(input("Enter number of transactions: "))

deposit_count = 0
successful_withdrawal_count = 0
rejected_withdrawal_count = 0

for i in range(1, transactions + 1):

    print("\nTransaction", i)

    transaction_type = input("Enter transaction type (Deposit/Withdrawal): ")
    amount = float(input("Enter amount: ₹"))

    if amount <= 0:
        print("Invalid transaction amount")

    elif transaction_type.lower() == "deposit":

        balance = balance + amount
        deposit_count = deposit_count + 1

        print("Transaction Status: Deposit Successful")
        print("Current Balance: ₹", balance)

    elif transaction_type.lower() == "withdrawal":

        if amount <= balance:
            balance = balance - amount
            successful_withdrawal_count = successful_withdrawal_count + 1

            print("Transaction Status: Withdrawal Successful")
            print("Current Balance: ₹", balance)

        else:
            rejected_withdrawal_count = rejected_withdrawal_count + 1

            print("Transaction Status: Withdrawal Rejected")
            print("Reason: Insufficient Funds")

    else:
        print("Invalid transaction type")

print("\n----- Bank Summary -----")
print("Final Balance: ₹", balance)
print("Deposit Count:", deposit_count)
print("Successful Withdrawal Count:", successful_withdrawal_count)
print("Rejected Withdrawal Count:", rejected_withdrawal_count)

if balance < 1000:
    print("Warning: Balance is below ₹1,000")