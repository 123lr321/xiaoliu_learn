def strStr(haystack, needle):
    for i in range(0, len(haystack)):
        if haystack[i:i + len(needle)] == needle:
            return i
    if i==len(haystack)-1:
        return -1
print(strStr('qwewasd','we'))