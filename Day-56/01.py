# Find all elements whose frequency is exactly K.

def find_element_of_frequency_k(nums , k):

    elements = []
    hash_map = {}

    for num in nums:
        if num in hash_map:
            hash_map[num] += 1

        else:
            hash_map[num] = 1

    for num in hash_map:
        if hash_map[num] == k:
            elements.append(num)

    return elements

print(find_element_of_frequency_k([1,2,2,3,4,5,3,6,9,6] ,2))