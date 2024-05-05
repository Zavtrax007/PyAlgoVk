from operator import contains


def twoSum(arr, target):
    if type(arr) is not list:
        raise TypeError('Arrays must be list')
    if type(target) is not int:
        raise TypeError('target must be integer')
    for i in range(len(arr)):
        if type(arr[i]) is not int:
            raise TypeError('Array  must contain integer')
    a_dict = {}
    for i in range(len(arr)):
        a_dict[arr[i]] = i
    for i in range(len(arr)):
        diff = target - arr[i]
        if contains(a_dict, diff):
            return [i, a_dict[diff]]

    return []
