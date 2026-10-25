#  Find all primes whose digit sum is also prime.

def prime_digits_prime(nums):

    def prime(num):
        if num < 2:
            return False

        for i in range(2 , int(num ** 0.5)+1):
            if num % i == 0:
                return False

        return True


    for i in range(1 , nums+1):

        if prime(i) == False:
            continue
        else:
            k = i
            is_prime = False
            while k > 0:
                last_digit = k % 10
                k = k // 10
                if prime(last_digit) == False:
                    is_prime = False
                    break
                else:
                    is_prime = True


            if is_prime == True:
                print(i)


prime_digits_prime(100)