def unicTree(n):
    if type(n) is not int:
        raise TypeError('n must be integer')
    if n < 1:
        raise ValueError('n must be positive')
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
