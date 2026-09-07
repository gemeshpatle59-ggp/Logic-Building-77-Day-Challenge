#  Find GCD of multiple numbers.

def find_muktiple_number_gcd():
    try:
        num = list(map(int,input("ENTER YOUR 1st NUMBER HERE.: ").split()))
        n = len(num)

        gcd = num[0]

        for i in range(1,n):
            a = gcd
            b = num[i]
            while b != 0:
                a ,b = b ,(a% b)
            gcd = a

        print("GCD =",gcd)

    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    find_muktiple_number_gcd()              