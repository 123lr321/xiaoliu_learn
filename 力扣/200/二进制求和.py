def addBinary( a, b):
    anw_list = [int(i) for i in str(int(a) + int(b))]
    for i in range(0, len(anw_list) - 1):
        if anw_list[i] == 2:
            anw_list[i] = 0
            anw_list[i + 1] += 1
        elif anw_list[i] == 3:
            anw_list[i] = 1
            anw_list[i + 1] += 1
    if anw_list[-1] == 2:
        anw_list[-1] = 0
        anw_list.append(1)
    elif anw_list[-1] == 3:
        anw_list[-1] = 1
        anw_list.append(1)
    anw_list.reverse()
    return ''.join(map(str,anw_list))
print(addBinary('11','11'))