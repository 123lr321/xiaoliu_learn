def group_anagrams(strs):
    strs_list = []
    anw = []
    for i_str in strs:
        strs_list.append("".join(sorted(i_str)))
    begin: int = 0
    end: int = 1
    i: int = 0
    while strs:
        anw.append([strs[0]])
        while end < len(strs):
            if strs_list[begin] == strs_list[end]:
                anw[i].append(strs[end])
                del strs[end]
                del strs_list[end]
            else:
                end = end + 1
        del strs[begin]
        del strs_list[begin]
        end = begin + 1
        i = i + 1
    return anw


print(group_anagrams(["a"]))
