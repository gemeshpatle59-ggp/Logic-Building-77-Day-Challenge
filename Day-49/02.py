# Find the suffix sums of an array.

def suffix_sum(arr):

    total = 0

    for i in arr:
        total += i


    suffix = []
    suffix.append(total)

    for i in range(len(arr)-1):
        total -= arr[i]
        suffix.append(total)


    return suffix

print(suffix_sum([5]))
