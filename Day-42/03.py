# Find the second largest distinct element.


def find_second_largest_distinct_value(arr):

    lar = 0
    sec_lar = 0

    for i in arr:
        if i > lar:
            sec_lar = lar
            lar = i

        else:
            if i != lar and i > sec_lar:
                sec_lar = i

        


    return sec_lar

print(find_second_largest_distinct_value([1,2,3,7,7,6]))

        