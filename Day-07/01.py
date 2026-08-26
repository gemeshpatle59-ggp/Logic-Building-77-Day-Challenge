# 1.	Print multiplication tables from 1 to N.


def multiplication_table():

    try:

        n = int(input("ENTER THE NUMBER HERE.: "))

        for j in range(1,n+1):
            print("---multiplication_table_of",(j),"---")
            for i in range(1,11):
                print(f"{j} x {i} = {n*i}")


    except ValueError:
        print("please enter the valid number.")

if __name__ == "__main__":
    multiplication_table()        