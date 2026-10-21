num = int(input("Enter a number:"))
sign = -1 if num < 0 else 1
num = abs(num)
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

reverse = reverse * sign
print("Reversed number =", reverse)