def minLength(s):
    def mininner(b):
        for i in range(0,len(b)):
            if b[i:i+2] == 'AB' or b[i:i+2] == 'CD':
                b=b[:i]+b[i+2:]
                return mininner(b)
        return len(b)
    return mininner(s)
print(minLength("ABFCACDB"))