#  Calculate x^n without using ** or pow().

def power():
    try:
        n= int(input("ENTER YOUR NUMBER HERE.: "))
        m= int(input("ENTER THE POWER HERE.: "))

        power = 1

        for _ in range(m):
            power *= n

        print(f"X^N = {power}")


    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    power()              