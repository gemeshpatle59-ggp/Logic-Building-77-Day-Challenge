# Check whether a string is a palindrome.

s = "abcba"

for i in range(len(s) // 2):
    if s[i] != s[len(s)-i-1]:
        print(False)
        break
else:
    print(True)