# Count even and odd elements.


def count_even_odd(nums):

    even = 0
    odd = 0


    for i in nums:
        if i % 2 == 0:
            even += 1

        else:
            odd += 1


    return (f"even_total = {even} , odd_total = {odd}")

print(count_even_odd([1,2,3,4,5,6,7,8,9,10]))