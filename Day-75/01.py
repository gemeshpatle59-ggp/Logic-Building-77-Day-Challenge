#  Create an expense analyzer that stores categories and amounts and reports totals, highest expense,category frequencies, and averages.

def expense_analyzer():

    expenses = {}
    frequency = {}

    n = int(input("Enter number of expenses: "))

    for i in range(n):

        category = input("Enter category: ").lower()
        amount = float(input("Enter amount: "))

        if category in expenses:
            expenses[category] += amount
            frequency[category] += 1
        else:
            expenses[category] = amount
            frequency[category] = 1

    # Total Expense
    total = 0

    for amount in expenses.values():
        total += amount

    # Highest and Lowest Expense
    highest = -1
    lowest = float('inf')

    highest_category = ""
    lowest_category = ""

    for category, amount in expenses.items():

        if amount > highest:
            highest = amount
            highest_category = category

        if amount < lowest:
            lowest = amount
            lowest_category = category

    # Average
    average = total / n

    # Report
    print("\n===== EXPENSE REPORT =====")

    print("\nCategory-wise Expenses:")

    for category, amount in expenses.items():
        print(category, ":", amount)

    print("\nTotal Expense:", total)

    print("Highest Expense:", highest_category, highest)

    print("Lowest Expense:", lowest_category, lowest)

    print("Average Expense:", average)

    print("\nCategory Frequencies:")

    for category, count in frequency.items():
        print(category, ":", count)

    print("\nExpenses Above 300:")

    for category, amount in expenses.items():
        if amount > 300:
            print(category, ":", amount)


if __name__ == "__main__":
    expense_analyzer()