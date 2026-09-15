#  Write a function to return the largest of three numbers.


def larger_number(n,m,o):
    if n > m and n > o:
        return ("larger number is", m)
    elif m > n and m > o:
        return ("larger number is", n)
    else:
        return ("larger number is", o)

print(larger_number(1,2,5))