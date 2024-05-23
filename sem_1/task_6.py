def zeroLast(arr):
    if type(arr) is not list:
        raise TypeError('arr must be list')
    i = len(arr) - 1
    j = 0
    while i > j:
        if arr[j] == 0 and arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        elif arr[i] == 0:
            i -= 1
        else:
            j += 1

    return arr
