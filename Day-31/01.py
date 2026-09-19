# Print N to 1 using recursion.

def n_to_one(n,i=1):
    if n < i:
        return
    print(n)
    n_to_one(n-1,i=1)

n_to_one(9)