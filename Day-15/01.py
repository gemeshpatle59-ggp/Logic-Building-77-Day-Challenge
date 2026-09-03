#  Print all prime numbers from 1 to N

def prime_number():
    try:
        n = int(input("ENTER THE NUMBER HERE.."))

        for num in range(2, n + 1):
            is_prime = True

            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print(num)

    except ValueError:
        print("please enter the integer ..") 

prime_number()
                   