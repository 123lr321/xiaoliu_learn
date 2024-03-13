from typing import List



def list_find(str_list):
    print(str_list)
    str_next = [0, 1]
    if str_list[0] == str_list[1]:
        str_next.insert(2, 2)
    else:
        str_next.insert(2, 1)
    for k in range(3, len(str_list) - 2):
        j = 2
        str_next.insert(k, 1)
        while j <= k:
            if str_list[1:j] == str_list[k - j + 1:k]:
                str_next[k] = j - 1
            j += 1
    return str_next


print(list_find(['a', 'b', 'a', 'a', 'e', 'a', 'a']))
list_exam: list[int] = [1, 2, 3, 4, 5]
it = iter(list_exam)
a = []
for i in range(0, len(list_exam)):
    b = [(next(it))]
    a[i:i + 1] = b
    print(a)
