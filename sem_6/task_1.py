def countSeq(n):
    if type(n) is not int:
        raise TypeError('n must be integer')
    if n < 0:
        raise ValueError('n must be positive')
    dp = [1, 2, 4]
    if n < 3:
        return dp[n]
    for i in range(n):
        dp.append((dp[i - 1] + dp[i - 2] + dp[i - 3]))
    return dp[n]



