# Reverse a string .

def reverse_string(num ):
    n = ""
    for i in range(len(num)-1,-1,-1):
        n += num[i]

    return n

print(reverse_string("gemesh"))