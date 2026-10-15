#  Find whether any two elements have a difference of K.

def find_difference_k(nums , k):

    elements = []
    seem = set()

    for num in nums:

        if num - k in seem:
            elements.append((num - k , num))

        if k - num in seem:
            elements.append((k - num , num))

        seem.add(num)

    return elements

print(find_difference_k([1,5,3,8] ,2))
