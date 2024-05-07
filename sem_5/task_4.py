def maxMinMulti(data):
    if type(data) is not list:
        raise TypeError('Array must be list')
    if len(data) < 1:
        return None
    if len(data) == 1:
        return data[0]*data[0]
    min_index = 1
    max_index = 2
    i = 0
    while i < len(data):
        min_index = i
        i = 2 * i + 1
    i = 0
    while i < len(data):
        max_index = i
        i = 2 * i + 2
    return data[min_index] * data[max_index]
