# 3.	Determine whether a triangle is acute, right, or obtuse using side lengths

def check_triangle():
    try:
        n = int(input("ENTER THE LENGTH OF 1ST SIDE HERE.: "))
        m = int(input("ENTER THE LENGTH OF 2ND SIDE HERE.: "))
        o = int(input("ENTER THE LENGTH OF 3RD SIDE HERE.: "))

        if n > 0 and m > 0 and o > 0:

            if n + m > o and n + o > m and m + o > n:
                if n >= m and n >= o:
                    if m**2 + (o**2) >  n**2:
                        print("Its acute angle triangle")

                    elif m**2 + (o**2) == n**2:
                        print("Its right angle triangle")

                    else:
                        print("Its obtuse angle triangle") 

                elif m >= n and m >= o:    
                    if n**2 + (o**2) >  m**2:
                        print("Its acute angle triangle")
                    
                    elif n**2 + (o**2) == m**2:
                        print("Its right angle triangle")
                    
                    else:
                        print("Its obtuse angle triangle") 

                else: 
                    if n**2 + (m**2) >  o**2:
                        print("Its acute angle triangle")
                    
                    elif n**2 + (m**2) == o**2:
                        print("Its right angle triangle")
                    
                    else:
                        print("Its obtuse angle triangle")    
                           
            else:
                print(f"The three sides {n}, {m}, {o} cannot form a triangle.")
        else:
            print("Zero or negative side cannot form a triangle.")
            
    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    check_triangle()