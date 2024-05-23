def delCop(s):
    if type(s) is not str:
        raise TypeError('s must be string')
    res = ''
    a = list(s)
    f, s = 0, 1
    while s < len(a):
        if len(a) < 2:
            break
        elif a[f] == a[s]:
            del a[s]
            del a[f]
            f, s = 0, 1
        else:
            f += 1
            s += 1
    return res.join(a)



