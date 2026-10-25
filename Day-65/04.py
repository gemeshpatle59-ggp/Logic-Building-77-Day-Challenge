# Find the number of ways to make a given amount using a small set of coin values using basic recursion.

def coin_change(coins, amount, index=0):

    if amount == 0:
        return 1

    if amount < 0 or index == len(coins):
        return 0

    # Current coin use karo
    use_coin = coin_change(coins, amount - coins[index], index)

    # Current coin use mat karo
    skip_coin = coin_change(coins, amount, index + 1)

    return use_coin + skip_coin


coins = [1, 2, 5]
amount = 5

print(coin_change(coins, amount))