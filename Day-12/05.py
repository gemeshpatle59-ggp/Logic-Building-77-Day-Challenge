#  Replace every occurrence of one digit with another.

num = 1234234
n = 4
m = 9

def replace_occurrance(num,n,m):
    num = str(num)
    n = str(n)
    m = str(m)
    result = ""
    for i in num:
        if i == n:
            result += m

        else:
            result += i    
            

    return int(result)        

print(replace_occurrance(num,n,m))