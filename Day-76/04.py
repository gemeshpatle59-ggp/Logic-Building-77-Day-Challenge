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


