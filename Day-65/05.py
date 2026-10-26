# Given daily values, find the best buy/sell pair for maximum profit using brute force, then optimize


def max_profit(prices):
    max_profit = 0
    buy_price = 0
    sell_price = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):

            profit = prices[j] - prices[i]

            if profit > max_profit:
                max_profit = profit
                buy_price = prices[i]
                sell_price = prices[j]

    print("Buy Price:", buy_price)
    print("Sell Price:", sell_price)
    print("Maximum Profit:", max_profit)


prices = [7, 1, 5, 3, 6, 4]
max_profit(prices)
