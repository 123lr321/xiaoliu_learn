def length_of_longest_substring(s):
        begin = 0
        end = 0
        anw = 0
        while end <= len(s):
            try:
                while end <= len(s):
                    if s[end] not in s[begin:end]:
                        end += 1
                    else:
                        anw = max(anw, end - begin)
                        begin += 1
                        end = begin
                        break
            except:
                anw = max(anw, end - begin)
                break
        return anw


print(length_of_longest_substring(" "))
a = '1223'
