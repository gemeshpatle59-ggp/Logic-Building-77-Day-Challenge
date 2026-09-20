#  Count digits recursively using integer operations.

def count_digit(num,i=0):
    if num == 0:
        return 0
    return count_digit(num//10) + 1

print(count_digit(1243))