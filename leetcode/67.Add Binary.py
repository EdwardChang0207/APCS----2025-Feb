def addBinary(a: str, b: str) -> str:
        while len(a) != len(b):
            if len(a) > len(b):
                b = '0' + b
            else:
                a = '0' + a
        b = '0' + b
        a = '0' + a
        a = list(map(int, list(a)))
        b = list(map(int, list(b)))
        t = 0
        for i in range(len(a)-1, -1, -1):
            a[i] += (b[i] + t)
            if a[i] >= 2:
                t = int(a[i] / 2)    
                a[i] %= 2
        if a[0] == 0: a.pop(0)
        r = ''
        for i in a:
             r += str(i)
        return r
print(addBinary('11','1'))