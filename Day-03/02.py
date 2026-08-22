# 2.	Determine whether a triangle is equilateral, isosceles, or scalene

def check_triangle():
    try:
        n = int(input("ENTER THE LENGTH OF 1ST SIDE HERE.: "))
        m = int(input("ENTER THE LENGTH OF 2ND SIDE HERE.: "))
        o = int(input("ENTER THE LENGTH OF 3RD SIDE HERE.: "))

        if n > 0 and m > 0 and o > 0:

            if n + m > o and n + o > m and m + o > n:
                print(f"The three sides {n}, {m}, {o} can form a triangle.")
            

                if n == m and n == o:
                    print("Its a Equilateral triangle.")

                elif n == m or m == o or o == n:
                    print("Its a Isosceles triangle.")

                elif n != m and m != o and o != n:
                    print("Its a Scalene triangle.")                

            else:
                print(f"The three sides {n}, {m}, {o} cannot form a triangle.")
        else:
            print("Zero or negative side cannot form a triangle.")
            
    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    check_triangle()