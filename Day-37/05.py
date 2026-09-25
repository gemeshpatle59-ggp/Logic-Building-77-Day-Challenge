# Find the most frequent character

def most_frequent_character(s):

    freq = {}
    most = 0
    max_char = ""

    for i in s:
        if i in freq:
            freq[i] += 1

        else:
            freq[i] = 1

    for char , value in freq.items():

        if value > most:
            most = value
            max_char = char

    return max_char

print(most_frequent_character("programming"))
    

