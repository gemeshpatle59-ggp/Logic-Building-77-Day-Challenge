# Determine time complexity of nested loops where both run n times.
n = 7


for i in range(n):
    for j in range(n):
        print(i, j)


"""

Outer loop runs N times.
For every outer iteration, the inner loop runs N times.
Total operations = N × N = N².

"""