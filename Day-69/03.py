# Find and fix a program that incorrectly handles 0.

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
else:
    print("Negative number")



num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")