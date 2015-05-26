#  https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


def maxProfit(prices):
    if len(prices) <= 1:
        return 0

    maxPrice = 0
    maxProfit = 0
    for i in reversed(xrange(len(prices))):
        if prices[i] > maxPrice:
            maxPrice = prices[i]
        maxProfit = max(maxProfit, maxPrice - prices[i])
    return maxProfit


def maxProfitFromStart(prices):
    if len(prices) <= 1:
        return 0

    minPrice = 0x7fffff
    maxProfit = 0
    for i in xrange(len(prices)):
        minPrice = min(minPrice, prices[i])
        maxProfit = max(maxProfit, prices[i] - minPrice)
    return maxProfit


if __name__ == '__main__':
    print maxProfit([1, 2])
    print maxProfit([1, 2, 3, 4, 5])
    print maxProfit([5, 8, 3, 7, 2, 6, 10, 30, 1, 28])

    print maxProfitFromStart([1, 2])
    print maxProfitFromStart([1, 2, 3, 4, 5])
    print maxProfitFromStart([5, 8, 3, 7, 2, 6, 10, 30, 1, 28])
