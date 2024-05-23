def reverseMas(li):
    if type(li) is not list:
        raise TypeError('Target must be list')

    left = 0
    r = len(li) - 1
    while left < r:
        li[left], li[r] = li[r], li[left]
        left += 1
        r -= 1
    return li
