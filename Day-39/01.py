# 1. Reverse the order of words in a sentence.

def reverse_sen(s):
    s = " " + s
    reversed_sentence = ""
    new_sen = ""

    for i in range(len(s) -1 , -1 , -1):
        if s[i] == " ":
            for j in range(len(new_sen)-1,-1,-1):
                reversed_sentence += new_sen[j]

            reversed_sentence += " "
            new_sen = ""

        else:
            new_sen += s[i]


    return reversed_sentence

print(reverse_sen("I am learning Python"))


