def findTheDifference(s,t):
    s_list=list(s)
    t_list=list(t)
    while len(t_list)>1:
        if t_list[0] in s_list:
            s_list.remove(t_list[0])
            del t_list[0]
        else:
            del t_list[1:]
    return ''.join(t_list)
print(findTheDifference('awd','wadq'))