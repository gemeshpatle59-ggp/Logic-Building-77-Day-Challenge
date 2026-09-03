#  Count prime numbers from 1 to N.

def count_prime():
    try:
        n = int(input("ENTER THE NUMBER HERE.: "))
        count = 0
        for num in range(2,n+1):
            is_prime = True

            for j in range(2 ,int(num ** 0.5) + 1):
                if num % j == 0:
                    is_prime = False
                    break
                    

            if is_prime:
                count += 1   

        return count

    except ValueError:
        print("Please enter the integer ..")

print(count_prime())
                  