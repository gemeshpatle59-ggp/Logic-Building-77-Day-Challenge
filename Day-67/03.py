# Given words, find the longest word that can be formed from another word's characters.

def longest_word(words):
    longest = ""

    for word in words:
        for other in words:
            if word != other and sorted(word) == sorted(other):
                if len(word) > len(longest):
                    longest = word

    return longest


words = ["cat", "tac", "act", "at", "dog"]
print(longest_word(words))