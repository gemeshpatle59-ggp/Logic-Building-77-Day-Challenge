# Count the frequency of one character.

def count_frequesncy(s,n):

    char_freq = 0

    for char in s:
        if char == n:
            char_freq += 1

    return (f"The frequency of character {n} in {s} is {char_freq}")

print(count_frequesncy("aaahhagsfaaydaa" , "a"))