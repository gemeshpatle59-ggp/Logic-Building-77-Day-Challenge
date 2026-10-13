# Find the first repeated element using a set.

def first_repeated_element_using_set(nums):
    
    seen = set()

    for num in nums:
        if num in seen:
            print(num)
            break

        seen.add(num)