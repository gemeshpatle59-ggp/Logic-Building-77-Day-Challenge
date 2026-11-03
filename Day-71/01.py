#  Determine time complexity of two consecutive loops.

n = 5

for i in range(n):
    print(i)

for j in range(n):
    print(j)

"""
First loop runs N times.
Second loop runs N times.
Total operations = N + N = 2N.
Ignore constants in Big-O notation.
"""