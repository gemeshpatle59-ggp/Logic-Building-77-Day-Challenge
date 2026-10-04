# Find the longest increasing contiguous run

def longest_increasing_run(l):

    current = 1
    longest = 1

    start = 0
    longest_start = 0
    longest_end = 0

    for i in range(len(l) - 1):

        if l[i] < l[i + 1]:
            current += 1

            if current > longest:
                longest = current
                longest_start = start
                longest_end = i + 1

        else:
            current = 1
            start = i + 1

    return l[longest_start:longest_end + 1], longest


print(longest_increasing_run([1, 2, 3, 2, 4, 5, 6, 1]))