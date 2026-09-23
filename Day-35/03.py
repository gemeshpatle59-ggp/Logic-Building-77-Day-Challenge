# Reverse a string without slicing.

s = "asfff"
rev = ""

for i in range(len(s)-1,-1,-1):
    rev += s[i]

print(rev)