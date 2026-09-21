# Check whether a string is palindrome recursively

def is_palindrome(s, start, end):
    if start >= end:
        return True

    if s[start] != s[end]:
        return False

    return is_palindrome(s, start + 1, end - 1)


s = "madam"

print(is_palindrome(s, 0, len(s) - 1))