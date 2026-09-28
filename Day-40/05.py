#  Find characters present in the first string but not the second.

def find_non_common_chr(s1 , s2):
    ans = ""

    for i in s1:
        if i not in s2:
            if i not in ans:
                ans += i

    print(ans)

find_non_common_chr("hello" , "world")