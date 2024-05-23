def binarySearchSqrt(target):
    if type(target) is not int:
        raise TypeError('Target must be integer')
    if target < 0:
        raise ValueError('Target must be positive')

    l = 0
    r = target
    while l <= r:
        middle = (l + r) // 2
        if middle ** 2 == target:
            return middle
        elif middle ** 2 > target:
            r = middle - 1
        elif middle ** 2 < target:
            l = middle + 1
    if (r + 1) ** 2 - target < target - r ** 2:
            return r + 1
    return r

