def romanToInt(s: str) -> int:
        t = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000} 
        k = list(t.keys())
        result = []
        for i in range(len(s)):
            if (i != len(s)-1) and not(s[i] in ['M','D']):
                if s[i+1] == (k[k.index(s[i])+1]):
                    result.append(-1*t[s[i]])
                elif s[i+1] == (k[k.index(s[i])+2]):
                    result.append(-1*t[s[i]])
                else: result.append(t[s[i]])
            else: result.append(t[s[i]])
        print(result)
        return sum(result)

print(romanToInt("MCMXCIV"))