# Count the frequency of every character.

def count_every_character_frequency(chars):

    hash_map = {}

    for char in chars:
        if char in hash_map:
            hash_map[char] += 1

        else:
            hash_map[char] = 0


    for key , value in hash_map.items():
        print(f"character = {key}\nfrequency = {value}\n")

count_every_character_frequency("aaaaaaahhhhhjjjjjj")