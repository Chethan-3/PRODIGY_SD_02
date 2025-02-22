import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Guess the number (between 1 and 100):")

    while not guessed_correctly:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the number in {attempts} attempts.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

guess_the_number()
