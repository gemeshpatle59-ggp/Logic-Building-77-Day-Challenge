#  Find the equilibrium index of an array.

def find_equilibrium_index_of_array(nums):

    total = 0
    left = 0

    for i in nums:
        total += i

    for j in range(len(nums)):
        
        temp = total - nums[j] 

        if left  == temp - left:
            return j

        left += nums[j]

    return f"no equilibrium index in the list"

print(find_equilibrium_index_of_array([1,2,3,2,1]))

         