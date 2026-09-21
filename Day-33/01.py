# Calculate x^n recursively.


def calculateXpowerN(n,i):
    if i == 0:
        return 1

    return n * calculateXpowerN(n , i-1)

print(calculateXpowerN(2,5))    
