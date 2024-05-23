def copyTime(n: int, x: float, y: float):
    if type(n) is not int or type(x) is not int or type(y) is not int:
        raise TypeError('Arguments must be integer')
    if n < 0 or x < 0 or y < 0:
        raise ValueError('Arguments must be positive')

    l = 0
    r = (n - 1) * max(x, y)
    while l + 1 < r:
        mid = (r + l) // 2
        if mid / x + mid / y < n - 1:
            l = mid
        else:
            r = mid

    return r + min(x, y)

