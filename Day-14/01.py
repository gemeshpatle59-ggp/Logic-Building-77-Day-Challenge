#  Check whether all digits of a number are unique.

num = 1234
my_set = set()

def unique(num):
    num = str(num)
    n = len(num)
    for i in range(n):
        if num[i] not in my_set:
            my_set.add(num[i])


        else:
            print("All digit in number is not unique..")    
            return

    print("All digits are unique..")    

unique(num)