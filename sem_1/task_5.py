
def chet(arr):
    if type(arr) is not list:
        raise TypeError('arr must be list')
    i = 0
    for j in range(len(arr)):
        if type(arr[i]) is not int:
            raise TypeError('arr must contain integers')
        if arr[j] % 2 == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return arr



