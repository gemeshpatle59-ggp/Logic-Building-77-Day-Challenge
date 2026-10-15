# Find missing values using set difference.

def find_missing(list1 , list2):

    seen1 = set(list1)
    seen2 = set(list2)

    missing = seen1 - seen2

    return missing

print(find_missing([1,2,3,4,5,6] , [2,3,4]))