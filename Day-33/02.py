# Find the maximum element of a list recursively.

def maxm_element(arr,nums):
    if nums == 0:
        return arr[0]

    max_of_rest = maxm_element(arr,nums-1)

    if arr[nums-1] > max_of_rest:
        return arr[nums-1]
    else:
        return max_of_rest