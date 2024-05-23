def reverseMas(li, l, r):
    if type(li) is not list:
        raise TypeError('li must be list')
    if type(l) is not int or type(r) is not int:
        raise TypeError('l and r must be integer')
    if l < 0 or r < l or r > len(li):
        raise ValueError('l and r must be in length of list')
    while l < r:
        li[l], li[r] = li[r], li[l]
        l += 1
        r -= 1
    return li


def lolRev(li, k):
    if type(li) is not list:
        raise TypeError('li must be list')
    if type(k) is not int:
        raise TypeError('k must be integer')
    if k < 0 or k > len(li):
        raise ValueError('k must be less length of list')
    n = len(li)
    reverseMas(li, 0, n - 1)
    reverseMas(li, 0, k)
    reverseMas(li, k + 1, n - 1)
    return li
