# Find common elements using sets.

def common_element_sing_sets(nums1 , nums2):


    set_a = set(a)
    set_b = set(b)

    common = set_a & set_b

    return common

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
print(common_element_sing_sets(a,b))