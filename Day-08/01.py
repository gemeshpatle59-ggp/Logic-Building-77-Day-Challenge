# 1. Count positive, negative, and zero values among N inputs.

class Count_numbers():
    def __init__(self,n):
        count = {
            "Positive" : 0,
            "Negative" : 0,
            "Zero" : 0
        }
        if n <= 0:
            print("inputs cannot be less than zero")
            return

        
        for _ in range(n):
            try:
                inputs = int(input("ENTER THE INPUT HERE.: "))
                if inputs > 0:
                    count["Positive"] += 1

                elif inputs < 0:
                    count["Negative"] += 1

                else:
                    count["Zero"] += 1               

            except ValueError:
                print("Please enter the valid number..")     

        print(count)                   

if __name__ == "__main__":
    Count_numbers(5)