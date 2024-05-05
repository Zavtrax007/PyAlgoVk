def groupAn(stroki):
    d = {}
    for s in stroki:
        sort_str = tuple(sorted(s))
        d[sort_str] = []
    for s in stroki:
        sort_str = tuple(sorted(s))
        d[sort_str].append(s)

    return (list(d.values()))


a = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat', 'eat']
print(groupAn(a))
