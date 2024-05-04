from operator import contains


def extraLetter(a, b):
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


a = 'bbabc'
b = 'bafbcb'
print(extraLetter(a, b))
