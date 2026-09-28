#  Find common characters between two strings.


def find_common_chr(s1 , s2):
    ans = ""

    for i in s1:
        if i in s2:
            if i not in ans:
                ans += i

    print(ans)

find_common_chr("hello" , "world")