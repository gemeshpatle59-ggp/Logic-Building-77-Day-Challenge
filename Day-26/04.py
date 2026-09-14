#  Create a pattern that prints only prime numbers in a triangular arrangement.


def patternprimetriangularnumber():

    try:
        n = int(input("ENTER YOUR LENGTH NUMBER HERE.: "))

        num = 2

        for i in range(1, n + 1):
            count = 0

            while count < i:
                prime = True

                for j in range(2, int(num ** 0.5) + 1):
                    if num % j == 0:
                        prime = False
                        break

                if prime:
                    print(num, end=" ")
                    count += 1

                num += 1

            print()                
                    
            
    except ValueError:
        print("Invalid input! Please enter an Integer.")

if __name__ == "__main__":
    patternprimetriangularnumber()             