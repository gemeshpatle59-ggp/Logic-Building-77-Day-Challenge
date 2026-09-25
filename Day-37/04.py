# Check whether two strings contain the same set of characters.

def check_two_string_contain_same_characte(s1, s2):

    if len(s1) > len(s2):
        sel = s1
    else:
        sel = s2
        
    hash_map = set()

    for i in sel:
        hash_map.add(i)

    if len(s1) < len(s2):
        sele = s1
    else:
        sele = s2

    for j in sele:
        if j not in hash_map:
            return False

    return True

print(check_two_string_contain_same_characte("abc" , "aabbcc"))