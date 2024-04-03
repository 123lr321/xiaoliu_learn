def find_anagrams(s,p):
        anw=[]
        for begin in range(0,len(s)):
            end = begin + len(p)
            if set(s[begin:end]) == set(p):
                p_test=p
                for i in s[begin:end]:
                    try:
                        p_test=p_test.replace(i,'',1)
                    except:
                        break
                if p_test=='':
                    anw.append(begin)
        return anw
print(find_anagrams("baa","aa"))