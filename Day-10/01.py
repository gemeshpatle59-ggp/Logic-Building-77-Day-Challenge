#  Find the smallest digit.

num = -453

def smallest_digit(num):
    num = abs(num)

    smallest = float("inf")
    while num > 0:
        last_digit = num % 10
        if smallest > last_digit:
            smallest = last_digit
        num = num // 10
        
    return smallest

print(f"smallest digit is {smallest_digit(num)}")  