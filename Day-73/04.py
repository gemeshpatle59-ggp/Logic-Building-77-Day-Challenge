# For each of five recursive programs, identify time and auxiliary space complexity.


"""
| No. | Recursive Program              | Time Complexity | Auxiliary Space Complexity |
|---  |---                             |---              |---                         |
| 1   | Factorial                      | O(n)            | O(n)                       |
| 2   | Fibonacci                      | O(2ⁿ)           | O(n)                       |
| 3   | Sum of first n natural numbers | O(n)            | O(n)                       |
| 4   | Binary Search                  | O(log n)        | O(log n)                   |
| 5   | Tower of Hanoi                 | O(2ⁿ)           | O(n)                       |

"""
# 1. Factorial

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Time: O(n), because the function is called n + 1 times.
# Auxiliary space: O(n), because the recursive call stack grows to n + 1 levels.


# 2. Fibonacci

def fibonacci(n):
    if n <= 1:        
        return n    
    return fibonacci(n - 1) + fibonacci(n - 2)


# - Time: O(2ⁿ), because each call generates two recursive calls.
# - Auxiliary space: O(n), because the maximum recursion depth is n.

# 3. Sum of First n Natural Numbers
def sum_n(n):    
    if n == 0:        
        return 0    
    return n + sum_n(n - 1)


# - Time: O(n), because the function makes n recursive calls.
# - Auxiliary space: O(n), because n recursive calls remain on the stack.


# 4. Binary Search
def binary_search(arr, low, high, target):    
    if low > high:        
        return -1    
    mid = (low + high) // 2    
    if arr[mid] == target:        
        return mid    
    elif arr[mid] < target:        
        return binary_search(arr, mid + 1, high, target)    
    else:        
        return binary_search(arr, low, mid - 1, target)


# - Time: O(log n), because the search space is halved in each recursive call.
# - Auxiliary space: O(log n), because the recursion depth is logarithmic


# 5. Tower of Hanoi
def hanoi(n):    
    if n == 1:        
        return    
    hanoi(n - 1)    
    hanoi(n - 1)


# - Time: O(2ⁿ), because each call generates two recursive calls.
# - Auxiliary space: O(n), because the maximum recursion depth is n.