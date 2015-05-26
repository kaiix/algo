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


if __name__ == '__main__':
    print maxProfit([1, 2])
    print maxProfit([1, 2, 3, 4, 5])
    print maxProfit([5, 8, 3, 7, 2, 6, 10, 30, 1, 28])
