# Find the first N prime numbers.


def first_n_prime():
    try: 
        n = int(input("ENTER THE NUMBER HERE.: "))
        num = 2
        count = 0
        while count < n:
            is_prime = True

            for i in range(2,int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime :
                print(num)
                count += 1

            num += 1

    except ValueError:
        print("Please enter the valid integer...") 

first_n_prime()
                   