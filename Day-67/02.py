# Given a string, remove consecutive duplicate characters repeatedly.

def remove_duplicates(s):
    stack = []

    for ch in s:
        if len(stack) > 0 and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return "".join(stack)

s = input("Enter a string: ")
print(remove_duplicates(s))
