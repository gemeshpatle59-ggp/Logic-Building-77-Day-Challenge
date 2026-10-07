# Find a triplet with a given sum.

def find_triplatee_with_given_sum(nums , s):

    nums.sort()

    for i in range(len(nums) - 2):

        left = i+1
        right = len(nums) - 1

        while left < right:

            total = nums[i] + nums[left] + nums[right]

            if total == s:
                return [nums[i] , nums[left] , nums[right]]

            elif total < s:
                i += 1

            else:
                right -= 1

    return None

print(find_triplatee_with_given_sum([2,4,3,7,5] , 9))

        

