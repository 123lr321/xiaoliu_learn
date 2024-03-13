

def repeated_substring_pattern(s):
    s = str(s)
    for i in range(1, len(s)):
        for k in range(0, i):
            for j in range(1, len(s)):
                if j * s[k:i] == s:
                    return True
    return False


print(repeated_substring_pattern('abacdefeeeeeabacdefeeeee'))
