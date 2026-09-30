# Find the kth largest element by logic, then compare with sorting

def kth_largest_element(arr,k):

    for i in range(len(arr)-1):
        is_swaped = False
        for j in range(i+1,len(arr)):
            if arr[j-1] > arr[j]:
                arr[j-1] , arr[j] = arr[j] , arr[j-1]
                is_swaped = True

        if is_swaped ==  False:
            break

    ele = 0
    for i in range(len(arr)-1,-1,-1):
        if k != 0:
            if arr[i] != ele:
                ele = arr[i]
                k -= 1
            if k == 0:
                return ele


print(kth_largest_element([1,2,4,6,3,7,4,5,9,3,4] , 3))




            

