# Build a number analyzer that reports digit count, sum, reverse, palindrome, prime, Armstrong, perfect, and
# digit frequencies


num = int(input("Enter a number: "))

n = abs(num)

# 1. Digit Count
temp = n
count = 0

if temp == 0:
    count = 1
else:
    while temp > 0:
        count += 1
        temp //= 10

# 2. Digit Sum
temp = n
digit_sum = 0

while temp > 0:
    digit_sum += temp % 10
    temp //= 10

# 3. Reverse
temp = n
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if num < 0:
    reverse = -reverse

# 4. Palindrome
if num == reverse:
    palindrome = True
else:
    palindrome = False

# 5. Prime Number
prime = True

if num < 2:
    prime = False
else:
    i = 2

    while i * i <= num:
        if num % i == 0:
            prime = False
            break
        i += 1

# 6. Armstrong Number
temp = n
armstrong_sum = 0

while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** count
    temp //= 10

if armstrong_sum == n:
    armstrong = True
else:
    armstrong = False

# 7. Perfect Number
perfect_sum = 0
i = 1

while i * i <= n:
    if n % i == 0:
        perfect_sum += i

        if i != n // i:
            perfect_sum += n // i

    i += 1

# Exclude the number itself
if n > 1:
    perfect_sum -= n

perfect = n > 1 and perfect_sum == n

# 8. Digit Frequencies
freq = [0] * 10

temp = n

if temp == 0:
    freq[0] = 1

while temp > 0:
    digit = temp % 10
    freq[digit] += 1
    temp //= 10

# Display Results
print("\n--- Number Analysis ---")

print("Digit Count:", count)
print("Digit Sum:", digit_sum)
print("Reverse:", reverse)

print("Palindrome:", "Yes" if palindrome else "No")
print("Prime:", "Yes" if prime else "No")
print("Armstrong:", "Yes" if armstrong else "No")
print("Perfect:", "Yes" if perfect else "No")

print("\nDigit Frequencies:")

for i in range(10):
    if freq[i] > 0:
        print(i, ":", freq[i])