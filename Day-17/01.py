#  Print all Armstrong numbers in a range.

def armstrong_number():

    try:
        num = int(input("ENTER THE RANGE OF NUMBERE HERE.: "))
        
        for j in range(1,num+1):
            total = 0
            i = j
            while i > 0:
                last_digit = i % 10
                total = total + (last_digit ** (len(str(i))))
                i = i // 10

            if (j == total)   :
                print(f"{j} is a armstrong number")
        


    except ValueError:
        print("Please enter the valid integer .")

(armstrong_number())                   

