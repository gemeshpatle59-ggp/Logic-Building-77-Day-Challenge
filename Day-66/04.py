# Given an array, find the maximum product of two distinct elements.

def max_product(array):
    n = len(array)
    maximum = float("-inf")

    for i in range(n):
        for j in range(i + 1, n):
            product = array[i] * array[j]

            if product > maximum:
                maximum = product

    return maximum


array = [3, 5, 1, 7, 2]
print(max_product(array))