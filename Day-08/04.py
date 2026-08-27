# Find the first number between 1 and N divisible by both A and B.

def Find_divisible():

    try:
        n = int(input("ENter the range number here.: "))
        a = int(input("Enter the 1st number here.: "))
        b = int(input("Enter thesecond number here.: "))
    except ValueError:
        print("Invalid input! Please enter an integer.") 
        return

    for i in range(1,n+1):
        if i % a == 0 and i % b == 0:
            return i
        
    print("Between 1 and ", n, "no number is divisible by", a, "and", b)   
             

if __name__ == "__main__":
    print(f"number : {Find_divisible()}")              