"""
Build a string analyzer that reports length, character frequencies, vowels, consonants, duplicates,
palindrome, and most frequent character.
"""


def string_analyzer(s):

    # length
    print(f"Length of String {s} is {len(s)}\n")

    # Character frequencies , duplicate , most frequent
    freq = {}
    duplicate = set()
    most_frequent = ""
    value = 0

    for i in s:
        if i in freq:
            freq[i] += 1
            duplicate.add(i)

        else:
            freq[i] = 1

        if freq[i] > 0:
            most_frequent = i
            value = freq[i]

    print(f"duplicate character are {duplicate}\n")
    print(f"Most Frequent character is {most_frequent}\n")
    print(f"character frequency are :")
    for key , value in freq.items():
        print(f"{key} : {value}")
    print()

    # vowels , cansonants

    vowels = {"a","e","i","o","u"}
    vovel = 0
    consonants = 0

    for i in s:
        if i in vowels:
            vovel += 1

        else:
            consonants += 1

    print(f"cansonants = {consonants} \nvowels = {vovel}")

    # Palindrome

    n = ""

    for i in range(len(s)-1 , -1 , -1):
        n += s[i]

    print(f"String is Palindrome : {n == s}")
    

if __name__ == "__main__":
    string_analyzer("gemeg")
