def Bubble_Sort(data:list, n:int)->list:
    for i in range(1,n):
        for j in range(n-i):
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp    
    return data

l = [5,4,3,2,1]
print(Bubble_Sort(l,5))