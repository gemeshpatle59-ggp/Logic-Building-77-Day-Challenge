# Determine complexity of a loop that doubles i each iteration.

n = 8
i = 1

while i < n:
    print(i)
    i = i * 2


"""

Explanation:

The values of i are:

$$ 1, 2, 4, 8, 16, 32 $$

After k iterations:

$$ i = 2^k $$

The loop stops when:

$$ 2^k >= N

Taking logarithm:

$$ k >= log_2 N 

Therefore, the loop runs approximately log₂N times.

O(log N)


"""