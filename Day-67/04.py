# Create a number guessing game and improve it with input validation and attempt counting.

import random

computer = random.randint(1, 100)
attemp = 0

while True:
    user_number = int(input("Enter The Number Here : "))
    attemp += 1

    if user_number > computer:
        print("Enter The Small Number")

    elif user_number < computer:
        print("Enter the larger number ")

    else:
        print(f"Correct Guess in {attemp} attemp")
        break

    