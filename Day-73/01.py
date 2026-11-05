#  Compare list membership with set membership conceptually.

"""
| Feature | List Membership | Set Membership |
|---|---|---|
| Syntax | `x in my_list` | `x in my_set` |
| Data structure | Ordered sequence | Unordered collection of unique elements |
| Search method | Checks elements one by one | Uses hashing to locate elements |
| Average time complexity | O(n) | O(1) |
| Worst-case time complexity | O(n) | O(n) |
| Duplicate elements | Allowed | Not allowed |
| Best use | When order and duplicates matter | When frequent membership checks are needed |

"""

numbers = [10, 20, 30, 40]
number_set = {10, 20, 30, 40}

print(30 in numbers)      # True
print(30 in number_set)   # True