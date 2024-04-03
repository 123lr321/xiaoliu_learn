def is_anagram(s, t):
    s_list=list(s)
    t_list=list(t)
    for i in s_list:
        if i in t_list:
            t_list.remove(i)
        else:
            return False
    if t_list!=[]:
        return False
    else:
        return True
print(is_anagram('waqw', 'wwaqa'))