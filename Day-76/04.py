# Create a final 'logic challenge' program that combines loops, functions, strings, lists, dictionaries, sets,
# recursion, and complexity analysis.


# 1 String Analyzer

def string_analyzer(text):

    words = text.split()

    print("\n--- STRING ANALYSIS ---")
    print("Total Characters:", len(text))
    print("Total Words:", len(words))
    print("Reversed String:", text[::-1])

    frequency = {}

    for ch in text:
        if ch != " ":
            if ch in frequency:
                frequency[ch] += 1
            else:
                frequency[ch] = 1

    print("Character Frequency:", frequency)


# 2. List Analyzer
def list_analyzer(nums):

    largest = nums[0]
    smallest = nums[0]
    total = 0

    for num in nums:

        if num > largest:
            largest = num

        if num < smallest:
            smallest = num

        total += num

    print("\n--- LIST ANALYSIS ---")
    print("Numbers:", nums)
    print("Largest:", largest)
    print("Smallest:", smallest)
    print("Sum:", total)
    print("Average:", total / len(nums))

# 3. Unique Number Finder Using Set
def unique_finder(nums):

    unique = set(nums)

    print("\n--- UNIQUE NUMBERS ---")
    print("Unique Numbers:", unique)
    print("Total Unique Numbers:", len(unique))

# 4. Dictionary Based Student Management
def student_manager():

    students = {}

    while True:

        print("\n--- STUDENT MANAGEMENT ---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display Students")
        print("4. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":

            name = input("Enter Name: ")
            marks = int(input("Enter Marks: "))

            students[name] = marks

            print("Student Added Successfully!")

        elif choice == "2":

            name = input("Enter Name: ")

            if name in students:
                print("Marks:", students[name])
            else:
                print("Student Not Found!")

        elif choice == "3":

            for name, marks in students.items():
                print(name, ":", marks)

        elif choice == "4":
            break

        else:
            print("Invalid Choice!")

# 5. Recursive Factorial
def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# 6. Prime Number Checker
def prime_checker(n):

    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# 7. Complexity Analysis
def complexity_analysis():

    print("\n--- COMPLEXITY ANALYSIS ---")

    print("Linear Search:")
    print("Time Complexity: O(n)")
    print("Space Complexity: O(1)")

    print("\nNested Loop:")
    print("Time Complexity: O(n^2)")
    print("Space Complexity: O(1)")

    print("\nBinary Search:")
    print("Time Complexity: O(log n)")
    print("Space Complexity: O(1)")

    print("\nRecursive Factorial:")
    print("Time Complexity: O(n)")
    print("Space Complexity: O(n)")


