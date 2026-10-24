# Find all numbers in a range whose digits are unique.

def unique_numbers(n , m):

    for i in range(n , m+1):
        seen = set()
        k = i
        bol = False
        while k > 0:
            last_digit = k % 10
            if last_digit in seen:
                bol = False
                break
            else:
                seen.add(last_digit)
                bol = True

            k = k//10

        if bol:
            print(i)

unique_numbers(10 , 100)