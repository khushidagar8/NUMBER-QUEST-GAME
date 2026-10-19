
import random

print("=" * 40)
print("       AI NUMBER GUESSING GAME")
print("=" * 40)

print("Hello, Player!")
print("I have selected a secret number from 1 to 100.")
print("Can you guess it?")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("\nEnter your guess: "))

        if guess < 1 or guess > 100:
            print("Please enter a number from 1 to 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try a bigger number.")
        elif guess > secret_number:
            print("Too high! Try a smaller number.")
        else:
            print("\nAmazing! You guessed it!")
            print("Secret number:", secret_number)
            print("Total attempts:", attempts)
            break

    except ValueError:
        print("Please enter a valid whole number.")

print("\nThanks for playing!")
