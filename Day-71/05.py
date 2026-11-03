# Determine complexity of a loop that halves n each iteration

n = 9

while n > 1:
    print(n)
    n = n // 2


"""

Explanation:

The values of N are:

    n , n/2 , n/4 , n/8 ,...

After k iterations:

    n/2^k  <= 1

Rearranging:

    n <= 2^k

Taking logarithm:

    k >= log^2n

Therefore, O(log N).


"""