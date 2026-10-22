# Daily Expense Tracker

days = int(input("Enter number of days: "))

total_expense = 0
highest_expense = 0

for i in range(1, days + 1):
    expense = float(input("Enter expense for day " + str(i) + ": ₹"))

    total_expense = total_expense + expense

    if expense > highest_expense:
        highest_expense = expense

average_expense = total_expense / days

print("\n----- Expense Summary -----")
print("Total Expense: ₹", total_expense)
print("Average Daily Expense: ₹", average_expense)
print("Highest Daily Expense: ₹", highest_expense)

if total_expense > 5000:
    print("Budget Status: Budget Alert")
else:
    print("Budget Status: Within Budget")