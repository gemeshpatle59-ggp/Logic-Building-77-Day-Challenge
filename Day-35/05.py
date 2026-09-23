# Count vowels and consonants in a string

s = "sjdgsgkgkagfA"

vovels = {'a','e','i','o','u'}

vovel = 0
consonants = 0


for i in s:
    if i.lower() in vovels:
        vovel += 1

    consonants += 1

print(f"vovel = {vovel}\nconsonants = {consonants}")

