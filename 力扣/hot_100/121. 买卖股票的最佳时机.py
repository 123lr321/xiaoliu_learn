def maxProfit(prices):
        anw = 0
        cost = float('+inf')
        for price in prices:
            cost = min(cost,price)
            anw = max(anw,price-cost)
        return anw
print(maxProfit([7,6,4,3,1]))
