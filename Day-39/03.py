# Check whether a string contains only digits.

def check_only_digits(s):

    for i in s :
        if 48 <= ord(i) <= 57:
            continue
        else:
            return False

    return True

print(check_only_digits("43254"))