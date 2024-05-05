from operator import contains


def extraLetter(a, b):
    if type(a) is not str or type(b) is not str:
        raise TypeError('a and b must be str')
    a_dict = {}
    for i in range(len(a)):
        a_dict[a[i]] = 0
    for i in range(len(a)):
        a_dict[a[i]] += 1

    for i in range(len(b)):
        if contains(a_dict, b[i]):
            a_dict[b[i]] -= 1
            if a_dict[b[i]] == 0:
                del a_dict[b[i]]
                continue
            continue
        return b[i]
    return ''
