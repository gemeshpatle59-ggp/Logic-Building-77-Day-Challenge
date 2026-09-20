# Reverse a number recursively.

def reverse_num(num , rev = 0):
    if num == 0:
        return rev
    last = num % 10
    rev = rev * 10 + last
    return reverse_num(num // 10,rev)

print(reverse_num(12))