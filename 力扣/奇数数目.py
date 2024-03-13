def countOdds(low, high):
    return len([i for i in range(low + 1, high) if i % 2 == 1])
print(countOdds(2,6))