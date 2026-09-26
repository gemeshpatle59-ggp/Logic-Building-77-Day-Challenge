# Find the shortest word in a sentence.

def shortest_sen(sen):

    shortest_sen1 = ""
    shortest_sen2 = ""

    for i in sen:
        if i == " ":

            if shortest_sen2 == "" or len(shortest_sen1) < len(shortest_sen2):
                shortest_sen2 = shortest_sen1

            shortest_sen1 = ""

        else:
            shortest_sen1 += i

    if shortest_sen2 == "" or len(shortest_sen1) < len(shortest_sen2):
        shortest_sen2 = shortest_sen1

    return shortest_sen2

print(shortest_sen("gemesh patle"))