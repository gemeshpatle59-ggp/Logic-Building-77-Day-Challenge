#  Find all pairs with a given sum


def find_pair_given_sum(nums , k):

    ans_pair = set()

    for i in range(len(nums)-1):
        pair = []
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == k:
                pair.append(nums[i])
                pair.append(nums[j])

                ans_pair.add(tuple(pair))

    
    return list(ans_pair)



print(find_pair_given_sum([2,3,5,6,7,1,4] , 7))