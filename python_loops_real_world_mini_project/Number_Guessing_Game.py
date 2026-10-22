# Number Guessing Game

secret_number = 37
attempts = 0
won = False

while attempts < 5:

    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        won = True
        break

    elif guess < secret_number:
        print("Too low")

    else:
        print("Too high")

if won == False:
    print("You lost!")
    print("The secret number was:", secret_number)

print("Attempts Used:", attempts)