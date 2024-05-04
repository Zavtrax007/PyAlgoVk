from operator import contains


def twoSum(arr, target):
    a_dict = {}
    for i in range(len(arr)):
        a_dict[arr[i]] = i
    for i in range(len(arr)):
        diff = target - arr[i]
        if contains(a_dict, diff):
            return [i, a_dict[diff]]

    return []


a = [1, 3, 4, 6, 5]
print(twoSum(a, 11))
