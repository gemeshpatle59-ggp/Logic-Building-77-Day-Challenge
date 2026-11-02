# Take one problem and intentionally create two wrong solutions; identify exactly why each fails.

# Wrong solution 1

arr = [10, 20, 30, 40]
largest = 0

for num in arr:
    if num > largest:
        largest = num

print(largest)

# Why it fails: Agar list mein saare numbers negative hain, toh largest ki value 0 hi rahegi.

# Wrong solution 2

arr = [10, 20, 30, 40]
largest = arr[0]

for num in arr:
    if num < largest:
        largest = num

print(largest)

# Why it fails: num < largest condition minimum number find karti hai, maximum nahi.

# Correct code:

arr = [10, 20, 30, 40]
largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print(largest)