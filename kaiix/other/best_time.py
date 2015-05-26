#  https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


def maxProfit(prices):
    if len(prices) <= 1:
        return 0

    m = 0
    for i in reversed(xrange(len(prices))):
        if prices[i] > m:
            m = prices[i]
        prices[i] = m - prices[i]
    return max(prices)


if __name__ == '__main__':
    print maxProfit([1, 2])
    print maxProfit([1, 2, 3, 4, 5])
    print maxProfit([5, 8, 3, 7, 2, 6, 10, 30, 1, 28])
