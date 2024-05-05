def sort_shell(arr: list):
    if type(arr) is not list:
        raise TypeError('Array must be list')
    n = len(arr)
    gap = len(arr) // 2 + 1
    while gap > 0:
        cur = gap
        while cur < n:
            m_gap = cur
            while m_gap >= gap and arr[m_gap] < arr[m_gap - gap]:
                arr[m_gap], arr[m_gap - gap] = arr[m_gap - gap], arr[m_gap]
            m_gap -= gap
            cur += 1
        gap = gap // 2
    return arr



