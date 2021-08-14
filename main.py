import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number from 1 to {x}: "))
        if guess > random_number:
            print("Guess is too high")
        elif guess < random_number:
            print("Guess too low")
    print(f"You guessed the right number {random_number}")

guess(10)