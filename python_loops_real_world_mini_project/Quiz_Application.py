# Quiz Application

score = 0
total_questions = 5

print("----- Python Quiz -----")

# Question 1
answer = input("1. Which keyword is used to define a function in Python? ")
if answer.lower() == "def":
    score = score + 1

# Question 2
answer = input("2. Which function is used to display output in Python? ")
if answer.lower() == "print":
    score = score + 1

# Question 3
answer = input("3. Which symbol is used for comments in Python? ")
if answer == "#":
    score = score + 1

# Question 4
answer = input("4. Which data type is used for True or False? ")
if answer.lower() == "bool":
    score = score + 1

# Question 5
answer = input("5. Which loop is commonly used with range()? ")
if answer.lower() == "for":
    score = score + 1

percentage = (score / total_questions) * 100

print("\n----- Quiz Result -----")
print("Score:", score, "/", total_questions)
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Performance: Excellent")

elif percentage >= 60:
    print("Performance: Good")

else:
    print("Performance: Keep Practicing")