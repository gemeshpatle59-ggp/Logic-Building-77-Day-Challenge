# 4.	Convert a score into a grade using conditions

def Convert_grade():
    try:
        n = float(input("ENTER YOUR SCORE HERE.."))

        if n >= 95:
            print("Your grade is 'A+' ")
        elif n >= 90:
            print("Your grade is 'A' ")
        elif n >=80:
            print("Your grade is 'B+' ")
        elif n >= 70:
            print("Your grade is 'B+' ")  
        elif n >= 50:
            print("Your grade is 'C' ")
        elif n >= 35:
            print("Your grade is 'D' ")
        else:
            print("FAIL..")        

    except ValueError:
        print("Please enter the valid score.")

if __name__ == "__main__":
    Convert_grade()
                
              
