from collections import deque

def isPalindromeStack(s):
    if type(s) is not str:
        raise TypeError('s must be string')

    stack = deque()
    for char in s:
        stack.append(char)

    for char in s:
        if char != stack.pop():
            return False

    return True


