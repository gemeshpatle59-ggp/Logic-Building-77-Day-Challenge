# Count vowels in a string recursively.

def count_vovel(stri,i=0):
    if stri == "":
        return i

    vovels = {'a','e','i','o','u'}
    if stri[0] in vovels:
        stri = stri[1:]
        return count_vovel(stri,i+1)

    stri = stri[1:]
    return count_vovel(stri,i)

print(count_vovel("abc"))