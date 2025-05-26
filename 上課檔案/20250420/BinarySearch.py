def BinarySearch(target, data):
    upper, lower = len(data)-1, 0
    mid = (upper+lower)//2
    while upper > lower:
        if data[mid] > target:
            upper = mid - 1
        elif data[mid] < target:
            lower = mid + 1
        else: return mid
        mid = (upper+lower)//2
    return -1

A = [1, 2, 3, 4, 5]
result = BinarySearch(10, A)
print(result)
