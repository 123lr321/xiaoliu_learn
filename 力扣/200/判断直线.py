def checkStraightLine(coordinates):
    if coordinates[1][0] - coordinates[0][0] == 0:
        return len({i[0] for i in coordinates}) == 1

    k = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
    for i in range(2, len(coordinates)):
        if coordinates[i][0] - coordinates[0][0] == 0:
            return False
        elif (coordinates[i][1] - coordinates[0][1]) / (coordinates[i][0] - coordinates[0][0])!=k:
            return False
    return True


print([1,-8],[2,-3],[1,2])
