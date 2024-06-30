import random

def number_guess_game():
    print("Welcome to MathMagnet")
    print("Are you feeling bored!")
    print("Come with me.....")
    print("I'm thinking of a number between 1 and 100.")

    hidden_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))

        if guess < hidden_number:
            print("Your number is too low, try again.")
        elif guess > hidden_number:
            print("Tour number is too high, try again.")
        else:
            print(f"Congratulations! You've guessed the number {hidden_number} correctly in {attempts} attempts.")
            break

        attempts += 1

number_guess_game()
