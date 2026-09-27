# Capitalize the first letter of every word without using title().

def capitalize_every_letter(s):

    n = 0
    capitlize_string = ""

    for i in range(len(s)):
        if 97 <= ord(s[i]) <= 122  and n == 0:
            capitlize_string += chr(ord(s[i]) - 32)
            n += 1
        elif s[i - 1] == " ":
            if 97 <= ord(s[i]) <= 122:
                capitlize_string += chr(ord(s[i]) - 32)

        else:
            capitlize_string += s[i]

    print(capitlize_string)


capitalize_every_letter("anchal patle jhhj hjkhui jhuhi ggiuh    hoi")
            