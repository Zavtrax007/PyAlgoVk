def sumCoins(coins, sum):
    if type(coins) is not list:
        raise TypeError('coins must be list')
    if type(sum) is not int:
        raise TypeError('sum must be integer')
    if sum < 0:
        raise ValueError('sum must be positive')
    for i in range(len(coins)):
        if type(coins[i]) is not int or coins[i] < 1:
            raise ValueError('coins must contain positive integers')
    count = 0
    for coin in reversed(coins):
        count += sum // coin
        sum = sum % coin
    if sum != 0:
        return -1
    return count
