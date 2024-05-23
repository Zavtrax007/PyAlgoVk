def isPalindromeP(s):
    if type(s) is not str:
        raise TypeError('s must be string')
    l = 0
    r = len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
