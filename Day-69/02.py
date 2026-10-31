# Find and fix an off-by-one error in a range loop.

#  error loop
def print_1_to_10():

    for i in range(1 ,10):
        print(i)


# correct_loop

def print_1_to_10():

    for i in range(1 , 11):
        print(i)