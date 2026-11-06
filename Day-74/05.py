"""
Create a student marks analyzer that calculates totals, averages, grades, highest scorer, lowest scorer, and
subject-wise statistics.

"""

# Student Marks Analyzer

students = {
    "Rahul": {"Python": 85, "Maths": 90, "English": 75},
    "Amit": {"Python": 70, "Maths": 65, "English": 80},
    "Rohit": {"Python": 95, "Maths": 88, "English": 92},
    "Priya": {"Python": 60, "Maths": 75, "English": 70},
    "Sneha": {"Python": 80, "Maths": 95, "English": 85}
}

subjects = ["Python", "Maths", "English"]

# Function to calculate total
def calculate_total(marks):
    return sum(marks.values())


# Function to calculate average
def calculate_average(marks):
    return calculate_total(marks) / len(marks)


# Function to calculate grade
def calculate_grade(avg):

    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


# 1. Student-wise Report
print("\n===== STUDENT REPORT =====")

for name, marks in students.items():

    total = calculate_total(marks)
    avg = calculate_average(marks)
    grade = calculate_grade(avg)

    print("\nName:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", round(avg, 2))
    print("Grade:", grade)


# 2. Highest Scorer
highest = None
highest_avg = -1

for name, marks in students.items():

    avg = calculate_average(marks)

    if avg > highest_avg:
        highest_avg = avg
        highest = name

print("\nHighest Scorer:", highest)
print("Highest Average:", highest_avg)


# 3. Lowest Scorer
lowest = None
lowest_avg = float('inf')

for name, marks in students.items():

    avg = calculate_average(marks)

    if avg < lowest_avg:
        lowest_avg = avg
        lowest = name

print("\nLowest Scorer:", lowest)
print("Lowest Average:", lowest_avg)


# 4. Subject-wise Statistics
print("\n===== SUBJECT STATISTICS =====")

for subject in subjects:

    total = 0
    highest_marks = -1
    lowest_marks = float('inf')

    top_student = ""
    low_student = ""

    for name, marks in students.items():

        score = marks[subject]
        total += score

        if score > highest_marks:
            highest_marks = score
            top_student = name

        if score < lowest_marks:
            lowest_marks = score
            low_student = name

    average = total / len(students)

    print("\nSubject:", subject)
    print("Average:", round(average, 2))
    print("Highest Marks:", highest_marks, "-", top_student)
    print("Lowest Marks:", lowest_marks, "-", low_student)