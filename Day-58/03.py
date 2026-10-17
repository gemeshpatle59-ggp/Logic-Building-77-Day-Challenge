# Find the longest substring without repeating characters.

def longest_substring(s):

    seen = set()
    left = 0
    temp = 0
    longest = 0

    while left < len(s):
        if s[left] in seen:
            if temp > longest:
                longest = temp
                
            temp = 0
            seen = set()

        else:
            seen.add(s[left])
            temp += 1
            left += 1


    if temp > longest:
        longest = temp

    return longest


print(longest_substring("abcabcbb"))