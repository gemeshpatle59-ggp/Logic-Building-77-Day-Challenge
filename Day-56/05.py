# Compare a nested-loop solution with a hashing solution and explain the time/space trade-off

# SOLUTION WITH NESTED LOOP...

def find_common(list1, list2):
    common = []

    for num1 in list1:
        for num2 in list2:
            if num1 == num2:
                common.append(num1)
                break

    return common

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70]

print(find_common(list1, list2))



# SOLUTION WITH THE HASHING.....

def find_common(list1, list2):
    seen = set(list2)
    common = []

    for num in list1:
        if num in seen:
            common.append(num)

    return common

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70]

print(find_common(list1, list2))


# | Feature               | Nested Loop      | Hashing (Set)       |
# | --------------------- | ---------------- | ------------------- |
# | Time Complexity       | `O(n × m)`       | `O(n + m)` average  |
# | Extra working space   | `O(1)`           | `O(m)`              |
# | Speed for large lists | Generally slower | Generally faster    |
# | Implementation        | Simple           | Thoda extra concept |
# | Memory usage          | Kam              | Zyada               |
