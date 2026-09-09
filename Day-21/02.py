# Convert binary to decimal without using int(..., 2)

def binary_decimal():
    try:
        n = input("ENTER YOUR NUMBER HERE.: ")

        if any(digit not in "01" for digit in n):
            print("Invalid binary number")
            return
        
        decimal = 0
        m = len(n)
        for i in range(m):
            decimal += (int(n[i])) * (2 ** (m-1-i))
            
        
        print(f"decimal = {decimal}")


    except ValueError:
        print("Invalid input! Please enter an Integer.")
    

if __name__ == "__main__":
    binary_decimal()              