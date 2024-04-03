def find_all_index(num, number):
    num = str(num)
    indexes = []
    for i in range(0, len(number)):
        start = number.find(str(num), i)
        if start == -1:
            break
        if start not in indexes:
            indexes.append(start)
        start += 1
    for i in range(0, len(indexes)):
        indexes[i] = (indexes[i] \
                      + 1)
    return indexes


num, xuyue_number = input("请输入需查找字符及电话号码,以逗号隔开（英文）").split(',')
print(find_all_index(num, xuyue_number))
