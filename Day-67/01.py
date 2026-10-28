# Given a string, determine whether brackets are balanced.

def balanced_bracket(s):
    stack = []

    for ch in s:
        if ch == "(" or ch == "[" or ch == "{":
            stack.append(ch)

        elif ch == ")" or ch == "]" or ch == "}":
            if len(stack) == 0:
                return False

            top = stack.pop()

            if ch == ")" and top != "(":
                return False

            elif ch == "]" and top != "[":
                return False

            elif ch == "}" and top != "{":
                return False

    return len(stack) == 0


s = "{[()]}"

if balanced_bracket(s):
    print("Balanced")
else:
    print("Not Balanced")