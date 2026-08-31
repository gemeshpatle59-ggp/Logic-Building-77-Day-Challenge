#  Remove the last digit of a number repeatedly and display each intermediate number.

num = 898924

def remove_last_digit(num):

    while num > 0:
        print(num)
        last_digit = num % 10
        num = num // 10

remove_last_digit(num)        
