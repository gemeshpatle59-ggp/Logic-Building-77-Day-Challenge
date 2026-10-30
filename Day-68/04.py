# Trace a recursive factorial call tree for 5.

def factorical(n):
    if n <= 1:
        return 1

    return n * factorical(n-1)

print(factorical(5))

"""
| Call | Function Call | Return Expression |
| ---- | ------------- | ----------------- |
| 1    | factorial(5)  | 5 × factorial(4)  |
| 2    | factorial(4)  | 4 × factorial(3)  |
| 3    | factorial(3)  | 3 × factorial(2)  |
| 4    | factorial(2)  | 2 × factorial(1)  |
| 5    | factorial(1)  | 1 (Base Case)     |


"""