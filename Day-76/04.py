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


