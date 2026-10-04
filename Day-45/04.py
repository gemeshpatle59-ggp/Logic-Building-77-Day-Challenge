# Check whether a list is sorted.

def check_list_is_sorted(l):

    j = 0

    while j < len(l) - 1 and l[j] == l[j+1]:
        j += 1


    if l[0] < l[1]:
        for i in range(j+1,len(l) -1 ):
            if l[i] > l[i+1]:
                return False


    else:
        for i in range(j+1,len(l) - 1):
            if l[i] < l[i+1]:
                return False

    return True

print(check_list_is_sorted([5,4,3,2,1,4]))