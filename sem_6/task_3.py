def pascal_triangle(row, col):
    if col == 0 or row == col:
        return 1
    else:
        return pascal_triangle(row - 1, col - 1)


def pascal(n):
    dp = []
    for i in range(n):
        tmp = []
        for j in range(i):
            tmp.append(1)
        dp.append(tmp)
    for row in range(1, n):
        for col in range(1, row):
            dp[row][col] = dp[row - 1][col - 1] + dp[row - 1][col]
