# Find and fix a program that incorrectly treats duplicate values as distinct 


numbers = [10, 20, 20, 30, 30, 30]

count = 0

for i in range(len(numbers)):
    count += 1

print(count)



numbers = [10, 20, 20, 30, 30, 30]

count = 0

for i in range(len(numbers)):
    if numbers[i] not in numbers[:i]:
        count += 1

print(count)