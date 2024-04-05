def merge(intervals):
    for j in range(0, len(intervals)):
        for k in range(0, j):
            if intervals[k][0] > intervals[j][0]:
                intervals[j], intervals[k] = intervals[k], intervals[j]
        i = 0
    while i < len(intervals) - 1:
        if intervals[i][1] >= intervals[i + 1][0]:
            intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
            del intervals[i + 1]
        else:
            i += 1
    return intervals


print(merge([[4, 5], [1, 4], [0, 1]]))
