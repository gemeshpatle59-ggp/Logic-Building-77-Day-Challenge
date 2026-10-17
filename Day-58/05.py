# Find the minimum sum of a subarray of fixed size K.

def manimum_sum_k_size(nums1 , k):

    longest = float("inf")
    temp1 = 0
    m = 0

    for i in range(k):
        temp1 += nums1[i]

    longest = temp1


    for j in range(k , len(nums1)):

        temp1 += nums1[j]
        temp2 = temp1 - nums1[m]
        temp1 -= nums1[m]

        if temp2 < temp1:
            if temp2 < longest:
                longest = temp2

        else:
            if temp1 < longest:
                longest = temp1

        m += 1

    return longest

arr = [2,3,4]
k = 2

print(manimum_sum_k_size(arr , k))