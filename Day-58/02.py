# Find intersection of two sorted arrays.


def intersection_two_sortedarray(arr1 , arr2):

    i = 0
    j = 0
    intersection = []

    while i < len(arr1) and j < len(arr2):

        if arr1[i] == arr2[j]:
            intersection.append(arr1[i])
            i += 1
            j += 1

        elif arr1[i] < arr2[j]:
            i += 1

        else:
            j += 1

    return intersection

print(intersection_two_sortedarray([1,2,3,4,5] , [2,3,5,6,7]))