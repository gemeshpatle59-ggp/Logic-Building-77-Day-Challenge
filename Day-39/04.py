# Check whether a string contains only alphabets.


def check_only_alphabet(s):

    for i in s:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            continue
        else:
            return False

    return True

print(check_only_alphabet("akhfgadwiu"))