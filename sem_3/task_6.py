def isSubsequence(a, b):
    if type(a) is not str or type(b) is not str:
        raise TypeError('Arguments must be string')
    f = 0
    s = 0
    while s < len(b):
        if a[f] == b[s]:
            f += 1
        s += 1
    return f == len(a)


