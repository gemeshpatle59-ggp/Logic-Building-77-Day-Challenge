# Count words without using split().

def count_word(sen):

    word = 0

    for i in sen:

        if i == " ":
            word += 1

    word += 1

    return word        

print(count_word("completed with 3 local objects"))