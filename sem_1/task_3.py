def merges_sorted_array(arr1, arr2):
    if type(arr1) is not list or type(arr2) is not list:
        raise TypeError('arr1 and arr2 must be sorted list')
    merged_array = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    merged_array += arr1[i:] + arr2[j:]
    return merged_array



