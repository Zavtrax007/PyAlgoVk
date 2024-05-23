def maxProfit(prices):
    if type(prices) is not list:
        raise TypeError('prices must be list')
    for i in range(len(prices)):
        if type(prices[i]) is not int or prices[i] < 1:
            raise ValueError('prices must contain positive integers')
    profit = 0
    min_price = prices[0]
    for currentPriceIndex in range(1, len(prices)):
        profit = max(profit, prices[currentPriceIndex] - min_price)
        min_price = min(min_price, prices[currentPriceIndex])
    return profit
