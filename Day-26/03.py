#  Create a pattern where spaces and symbols depend on row number.

def patternspacesymbolsonrow():

    try:
        n = int(input("ENTER YOUR LENGTH NUMBER HERE.: "))

        for i in range(1,n+1):
            print(" "*(n-i) + ("*"*((i*2)-1)))
            
    except ValueError:
        print("Invalid input! Please enter an Integer.")

if __name__ == "__main__":
    patternspacesymbolsonrow()             