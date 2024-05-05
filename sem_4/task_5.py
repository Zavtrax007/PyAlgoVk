def groupAn(stroki):
    if type(stroki) is not list:
        raise TypeError('Array must be list')
    for i in range(len(stroki)):
        if type(stroki[i]) is not str:
            raise TypeError('Array  must contain strings')
    d = {}
    for s in stroki:
        sort_str = tuple(sorted(s))
        d[sort_str] = []
    for s in stroki:
        sort_str = tuple(sorted(s))
        d[sort_str].append(s)

    return (list(d.values()))


