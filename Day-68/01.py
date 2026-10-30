# Trace a reverse-number algorithm for 1200 and explain the output.

n = 1200
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print(rev)



"""
| Iteration |    n | digit = n % 10 | rev = rev * 10 + digit | n = n // 10 |
| --------- | ---: | -------------: | ---------------------: | ----------: |
| 1         | 1200 |              0 |                      0 |         120 |
| 2         |  120 |              0 |                      0 |          12 |
| 3         |   12 |              2 |                      2 |           1 |
| 4         |    1 |              1 |                     21 |           0 |


"""