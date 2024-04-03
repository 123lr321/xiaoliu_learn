def maxProfit(prices):
    profit = 0
    n = 0
    for i in range(0, len(prices)):
        for j in range(i, len(prices)):
            if prices[j] - prices[i] > profit:
                profit = prices[j] - prices[i]
                n = j + 1
    if profit > 0:
        return n
    else:
        return 0
print((maxProfit([7,1,5,3,6,4])))