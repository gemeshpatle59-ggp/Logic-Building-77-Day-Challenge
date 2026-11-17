# Create a command-line number guessing game with difficulty levels, hints, and attempt statistics.

import random

# Function to select difficulty
def select_difficulty():

    print("\nSelect Difficulty:")
    print("1. Easy (1-20) - 7 Attempts")
    print("2. Medium (1-50) - 5 Attempts")
    print("3. Hard (1-100) - 7 Attempts")

    while True:
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            return 20, 7

        elif choice == "2":
            return 50, 5

        elif choice == "3":
            return 100, 7

        else:
            print("Invalid choice! Try again.")


# Function to play game
def play_game():

    maximum, attempts = select_difficulty()

    number = random.randint(1, maximum)

    count = 0
    won = False

    print("\nGuess a number between 1 and", maximum)
    print("You have", attempts, "attempts.")

    while count < attempts:

        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > maximum:
                print("Enter a number within the given range!")
                continue

        except ValueError:
            print("Please enter a valid integer!")
            continue

        count += 1

        if guess == number:
            print("\nCongratulations! You guessed correctly.")
            won = True
            break

        elif guess < number:
            print("Hint: Your guess is too LOW!")

        else:
            print("Hint: Your guess is too HIGH!")

        # Additional hint
        if count == 2:
            if number % 2 == 0:
                print("Extra Hint: The number is EVEN.")
            else:
                print("Extra Hint: The number is ODD.")

        print("Attempts remaining:", attempts - count)

    # Game statistics
    print("\n===== GAME STATISTICS =====")

    print("Secret Number:", number)
    print("Total Attempts:", count)

    if won:
        print("Result: WIN")
        print("Remaining Attempts:", attempts - count)

    else:
        print("Result: LOSE")
        print("Correct Number was:", number)


# Main program
while True:

    play_game()

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("\nThanks for playing!")
        break