#  Compress repeated characters, e.g. aaabbc -> a3b2c1.

def compress_chr(s):

    temp = 1
    compress_str = ""

    i = 0
    j = 1

    while j < len(s):

        if s[j] == s[i]:
            temp += 1
            i += 1
            j += 1

        else:
             compress_str += s[i] + str(temp)
             temp = 1
             i +=1
             j += 1
    compress_str += s[i] + str(temp)

    return compress_str

print(compress_chr("aaabccc"))

        

        