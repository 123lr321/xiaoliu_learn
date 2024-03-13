def merge_two_list(list1, list2):
    list1.sort
    list2.sort
    list_results = []
    j = 0
    k = 0
    for i in range(0, len(list1) + len(list2) - 1):
        if list1[j] < list2[k]:
            list_results.append(list1[j])
            j += 1
        else:
            list_results.append(list2[k])
            k += 1
    if len(list2) > len(list1):
        list_results.append(list2[-1])
    else:
        list_results.append(list1[-1])
    return list_results


print(merge_two_list([1, 2, 4], [1, 3, 4]))
