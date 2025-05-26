def LinearSeach(target, data):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

A = [40, 31, 2, 6, 18]
result = LinearSeach(27,A)
print(result)