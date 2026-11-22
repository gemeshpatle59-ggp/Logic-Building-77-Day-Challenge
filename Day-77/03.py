# Find the longest word with all unique characters in a sentence.

def longest_unique_word_character(sen):

    unique_word = ""

    for word in sen.split():

        freq = {}
        valid = True

        for char in word:

            if char in freq:
                valid = False
                break

            freq[char] = 1

        if valid and len(word) > len(unique_word):
            unique_word = word

    return unique_word


print(longest_unique_word_character("hello gemesh python world"))