def count_seq(n):
    dp = [1, 2, 4]
    if n < 3:
        return dp[n]
    for i in range(n):
        dp.append((dp[i - 1] + dp[i - 2] + dp[i - 3]))
    return dp[n]
