def pascal_triangle(row, col):
    if col == 0 or row == col:
        return 1
    else:
        return pascal_triangle(row - 1, col - 1) + pascal_triangle(row - 1, col)


def pascal(n):
    if type(n) is not int:
        raise TypeError('n must be integer')
    dp = []
    for i in range(n):
        curRow = []
        for j in range(i + 1):
            curRow.append(pascal_triangle(i, j))
        dp.append(curRow)
    return dp


def iterPascal(n):
    if type(n) is not int:
        raise TypeError('n must be integer')
    dp = []
    for i in range(n):
        tmp = []
        for j in range(i + 1):
            tmp.append(1)
        dp.append(tmp)
    for row in range(1, n):
        for col in range(1, row):
            dp[row][col] = dp[row - 1][col - 1] + dp[row - 1][col]
    return dp



