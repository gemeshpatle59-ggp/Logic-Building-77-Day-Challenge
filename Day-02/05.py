# 5.	Build a simple calculator using an operator as input

def calculator():
    try:
        n = int(input("ENTER THE FIRST NUMBER HERE.: "))
        m = input("ENTER THE OPERATOR HERE.: ")
        o = int(input("ENTER THE SECOND NUMBER HERE.: "))

        if m == "+":
            print(f"{n+o}")

        elif m == "-":
            print(f"{n-o}")

        elif m == "*":
            print(f"{n*o}")

        elif m == "/":
            if o == 0:
                print(n," is cannot divide by Zero")
            else:    
                print(f"{n/o}")

        else:
            print(f"{m} is not a valid oprator")    

    except ValueError:
        print("Please enter the valid input num ber and oprator.")                    


if __name__ == "__main__":
    calculator()