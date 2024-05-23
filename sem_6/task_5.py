def maxProfit(prices):
    profit = 0
    min_price = prices[0]
    for currentPriceIndex in range(1, len(prices)):
        profit = max(profit, prices[currentPriceIndex] - min_price)
        min_price = min(min_price, prices[currentPriceIndex])
    return profit
