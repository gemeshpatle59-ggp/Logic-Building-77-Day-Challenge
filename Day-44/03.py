# Check whether two lists are equal.

def check_two_list_equal(l1 , l2):

    if len(l1) != len(l2):
        return False

    for i in range(len(l1)):

        if l1[i] != l2[i]:
            return False

    return True

print(check_two_list_equal([1,2,3,4,5] , [1,2,3,4,5]))