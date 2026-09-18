#  Print 1 to N using recursion

def one_to_n(n,i=1):
    if i > n:
        return
    print(i)
    one_to_n(n,i+1)


one_to_n(10)