# 1.	Check whether three sides can form a triangle.

def check_triangle():
    try:
        n = int(input("ENTER THE LENGTH OF 1ST SIDE HERE.: "))
        m = int(input("ENTER THE LENGTH OF 2ND SIDE HERE.: "))
        o = int(input("ENTER THE LENGTH OF 3RD SIDE HERE.: "))

        if n > 0 and m > 0 and o > 0:

            if n + m > o and n + o > m and m + o > n:
                print(f"The three sides {n}, {m}, {o} can form a triangle.")

            else:
                print(f"The three sides {n}, {m}, {o} cannot form a triangle.")

        else:
            print("Zero or negative side cannot form a triangle.")

    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    check_triangle()