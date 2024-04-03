def minimum_removal(beans):
    beans.sort()
    n = len(beans)
    lit = []
    for i in range(0, n):
        lit.append((n-i)*beans[i])
    return sum(beans) - max(lit)


print(minimum_removal([4, 1, 6, 5]))
