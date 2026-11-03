# Determine complexity when an inner loop runs from 1 to i.
n = 8

for i in range(n):
    for j in range(i):
        print(i, j)


"""

The inner loop runs different numbers of times:

Outer loop (i)	Inner loop iterations
0	0
1	1
2	2
3	3
...	...
N-1	N-1

Total operations:

0+1+2+3+⋯+(N−1)

Using the sum formula:

$$ \frac{N(N-1)}{2} $$

Ignoring constants and lower-order terms:

O(N²)

"""