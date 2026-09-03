#  Find the sum of all primes up to N.

def prime_sum():

    try:
        n = int(input("ENTER THE NUMBER HERE.: "))

        sum = 0

        for num in range(2,n+1):
            is_prime = True

            for i in range(2,int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                sum += num

        print(f"sum : {sum}") 

    except ValueError:
        print("Please enter the integer here..")    

prime_sum()
                   