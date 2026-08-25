# 5.	Print the multiplication table of a number.

def multiplication_table():

    try:

        n = int(input("ENTER THE NUMBER HERE.: "))

        print("---multiplication_table_of",(n),"---")

        for i in range(1,11):
            print(f"{n} x {i} = {n*i}")


    except ValueError:
        print("please enter the valid number.")

if __name__ == "__main__":
    multiplication_table()        