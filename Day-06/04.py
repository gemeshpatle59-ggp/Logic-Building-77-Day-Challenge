# 4.	Count how many numbers from 1 to N are divisible by K

def divisible_k():

    try:
        n = int(input("ENTER THE NUMBER HERE.: "))
        k = int(input("ENTER THE NUMBER TO CHECK DIVISIBLE BY .: "))

        divisible_k = 0

        for i in range(1,n+1):
            if i % k == 0:

                divisible_k += 1

        print(divisible_k)

    except ValueError:
        print("please enter the valid number.")
        
if __name__ == "__main__":
    divisible_k()