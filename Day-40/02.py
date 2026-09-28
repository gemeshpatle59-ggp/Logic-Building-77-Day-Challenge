# Remove a chosen character without using replace().

def remove_char(s,h):

    ans = ""

    for i in s:
        if i == h:
            continue
        else:
            ans += i

    return ans

print(remove_char("gemesh","e"))
