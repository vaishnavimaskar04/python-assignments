# Electricity Usage Analyzer

days = int(input("Enter number of days: "))

total_units = 0
high_usage_days = 0
maximum_usage = 0

for i in range(1, days + 1):

    units = float(input("Enter electricity usage for day " + str(i) + ": "))

    total_units = total_units + units

    if units > 10:
        high_usage_days = high_usage_days + 1

    if units > maximum_usage:
        maximum_usage = units

average_usage = total_units / days

print("\n----- Electricity Usage Summary -----")
print("Total Units:", total_units)
print("Average Usage:", average_usage)
print("High-Usage Days:", high_usage_days)
print("Maximum Daily Usage:", maximum_usage)

if total_units > 300:
    print("Usage Status: High Usage")
else:
    print("Usage Status: Normal Usage")