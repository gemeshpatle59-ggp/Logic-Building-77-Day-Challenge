#  Count uppercase, lowercase, digits, and special characters.

def countUpperlowerdigitSpical(s):
    lowercase = 0
    uppercase = 0
    digits = 0
    spical = 0


    for i in s:

        if 97 <= ord(i) <= 122:
            lowercase += 1

        elif 65 <= ord(i) <= 90:
            uppercase += 1

        elif 48 <= ord(i) <= 57 :
            digits += 1

        else:
            spical += 1


    return (f"lowercase character = {lowercase} \nuppercase character = {uppercase} \ndigits = {digits} \nspical = {spical}")

print(countUpperlowerdigitSpical("gsyq35ergs137ebrxyr2"))
