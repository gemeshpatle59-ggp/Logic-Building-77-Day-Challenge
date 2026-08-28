#  Find the product of digits.

num = -453

def product_digit(num):
    num = abs(num)

    product = 1
    while num > 0:
        last_digit = num % 10
        product *= last_digit
        num = num // 10
        
    return product

print(product_digit(num))    