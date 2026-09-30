# Find the second smallest distinct element.

def find_second_smallest_element(arr):

    smallest = float("inf")
    sec_smallest = float("inf")

    for i in arr:
        if i < smallest:
            sec_smallest = smallest
            smallest = i

        else:
            if i != smallest and i < sec_smallest:
                sec_smallest = i

    return sec_smallest 

print(find_second_smallest_element([1,5,6,3,7,9,4]))
