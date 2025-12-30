from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempt = 10 if choice == "easy" else 5
result = random.randint(1,101)
should_continue = True
while should_continue:
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess != result:
        if guess < result:
            print("Too low.\nGuess again.")
        else:
            print("Too high.\nGuess again.")
        attempt -= 1
        if attempt <= 0:
            print("You've run out of guesses. Refresh the page to run again.")
            should_continue = False
    else:
        print(f"You got it! The answer was {result}.")
        should_continue = False