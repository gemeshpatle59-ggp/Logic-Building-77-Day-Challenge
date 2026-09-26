# Reverse every word in a sentence

def reverse_sen(sen):

    sentence = ""
    n = 0
    m = 0
    for i in range(len(sen)):
        if sen[i] == " ":
            for j in range(i-1 , m-1 , -1):
                sentence += sen[j]

            sentence += " "
            m = i + 1


    for k in range(len(sen) - 1 , m-1 , -1):
        sentence += sen[k]

    return sentence

print(reverse_sen("completed with 2 local objects"))

