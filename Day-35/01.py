# Convert a loop-based solution into recursion and compare time/space complexity.

# que.:  findd the sum of 1 to n :

# this solution is on loop-based , used for loop

n = int(input("ENTER THE NUMBER HERE.: "))

total = 0

for i in range(1,n+1):    
    total += i

print(total)    

# time complexcity is o(n) one for loop is running n times
# space complexcity is o(1) hence  one extra variable is added 'total'


# same solution using recursion based using function under the function.

def sum_n(num , i=0):
    # base case statement:
    if num == 0:
        return i

    i += num

    return sum_n(num -1 , i)

print(sum_n(10))

# time complexcity is o(n) one for loop is running n times
# space complexcity is o(n) 
