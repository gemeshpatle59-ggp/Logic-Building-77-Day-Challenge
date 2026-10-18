#  Find the smallest subarray with sum at least s.



def smallest_subarray(nums , s):

    left = 0
    temp_sum = 0
    min_length = float("inf")

    for right in range(len(nums)):

        temp_sum += nums[right]

        while temp_sum >= s:

            length = right - left + 1

            if length < min_length:
                min_length = length

            temp_sum -= nums[left]
            left += 1

    if min_length == float("inf"):
        return 0

    return min_length


nums = [2, 3, 1, 2, 4, 3]
s = 7

print(smallest_subarray(nums, s))