# Find all positions of a given character

def find_position_of_given_character(s,a):

    freq = []

    for i in range(len(s)):
        if s[i] == a:
            freq.append(i)
            

    return freq

print(find_position_of_given_character("banana is / haaj - = 8 7 6* & ^ % 4 3/" , "a"))

