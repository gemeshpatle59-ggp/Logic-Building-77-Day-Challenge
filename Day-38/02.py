#  Find the longest word in a sentence.

def longest_word(sen):


    longest_sen1 = ""
    longest_sen2 = ""

    for i in sen:
        if i == " ":
            if len(longest_sen1) > len(longest_sen2):
                longest_sen2 = longest_sen1
            longest_sen1 = ""

        else:
            longest_sen1 += i

        if len(longest_sen1) > len(longest_sen2):
            longest_sen2 = longest_sen1


    return longest_sen2

print(longest_word("gemesh patle"))
