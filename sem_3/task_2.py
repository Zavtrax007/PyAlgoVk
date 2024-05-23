from collections import deque


def isSubsequence(a, b):
    if type(a) is not str or type(b) is not str:
        raise TypeError('Arguments must be string')
    dq = deque()
    for el in a:
        dq.append(el)

    for el in b:
        eq = dq.popleft()
        dq.appendleft(eq)
        if eq == el:
            dq.popleft()

    if len(dq) != 0:
        return False
    else:
        return True
