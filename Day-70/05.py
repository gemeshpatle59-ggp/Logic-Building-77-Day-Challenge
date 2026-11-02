# Determine time complexity of a single loop running N times

n = int(input("Enter n: "))

for i in range(n):
    print(i)

# Loop n times execute hota hai.
# Har iteration mein constant time ka kaam hota hai.
# Total operations approximately n ke proportional hain.


# Time complexity: O(N)
# Space complexity: O(1), kyunki extra memory input size ke saath increase nahi hoti.
# Example: Agar n = 100, toh loop 100 times chalega. Agar n = 1000, toh 1000 times chalega.