#  Replace a character without using replace().

def replace_chr(s,r,w):

    ans = ""
    for i in s:
        if i == r:
            ans += w

        else:
            ans += i

    return ans


print(replace_chr("gemesh" , "g" ,"h"))
