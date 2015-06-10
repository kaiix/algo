#  https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


def maxProfit(prices):
    maxProfit = 0
    for i in xrange(len(prices)-1):
        if prices[i+1] > prices[i]:
            maxProfit += (prices[i+1]-prices[i])
    return maxProfit

if __name__ == '__main__':
    print maxProfit([1, 2])
    print maxProfit([3, 2, 6, 5, 0, 3])
