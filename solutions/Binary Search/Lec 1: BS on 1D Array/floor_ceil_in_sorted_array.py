def getFloorAndCeil(a, n, x):
    start = 0
    end = n - 1

    floor = ceil = -1

    while start <= end:
        mid = start + ((end - start) // 2)
        if a[mid] >= x:
            ceil = a[mid]
            end = mid - 1
        if a[mid] <= x:
            floor = a[mid]
            start = mid + 1

    return [floor, ceil]