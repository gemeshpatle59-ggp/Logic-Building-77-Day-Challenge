#  Merge two sorted arrays using two pointers.


def merge_teo_sorted_array(nums1 , nums2):

    i = 0
    j = 0
    result = []

    while i < len(nums1) and j < len(nums2):

        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1

        else:
            result.append(nums2[j])
            j += 1


    while i < len(nums1):
        result.append(nums1[i])
        i += 1

    while j < len(nums2):
        result.append(nums2[j])
        j += 1

    return result

print(merge_teo_sorted_array([1,2,4,5] , [3,4,6,7,8]))
