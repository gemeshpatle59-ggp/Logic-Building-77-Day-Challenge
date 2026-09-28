# Check whether one string is a rotation of another.


def check_rotation_str(s , t):

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] != t[len(t)-i-1]:
            return False

    return True

print(check_rotation_str("gemesh" , "hseme"))