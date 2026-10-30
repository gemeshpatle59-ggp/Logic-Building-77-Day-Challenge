# Dry-run Armstrong logic for 153, 370, and 123.

def armstrong_num(num):
    n = num
    arm = 0

    while n > 0:
        last_digit = n % 10
        arm += last_digit**len(str(num))
        n = n // 10

    return num == arm

print(armstrong_num(153))

"""
| Iteration |   n | digit | digit ** 3 | total | n // 10 |
| --------- | --: | ----: | ---------: | ----: | ------: |
| 1         | 153 |     3 |         27 |    27 |      15 |
| 2         |  15 |     5 |        125 |   152 |       1 |
| 3         |   1 |     1 |          1 |   153 |       0 |


"""