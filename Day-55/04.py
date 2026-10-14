# Group words that are anagrams.

def group_anagrams(words):
    hash_map = {}

    for word in words:
        key = "".join(sorted(word))

        if key not in hash_map:
            hash_map[key] = []
        
        hash_map[key].append(word)

    return list(hash_map.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(words))


