def merges_sorted_array(arr1, arr2):
    if type(arr1) is not list or type(arr2) is not list:
        raise TypeError('arr1 and arr2 must be sorted list')
    i = len(arr1) - len(arr2) - 1
    j = len(arr2) - 1
    p = len(arr1) - 1

    while j >= 0:
        if i >= 0:
            if arr1[i] > arr2[j]:
                arr1[p] = arr1[i]
                i -= 1
            else:
                arr1[p] = arr2[j]
                j -= 1
        p -= 1
    return arr1



