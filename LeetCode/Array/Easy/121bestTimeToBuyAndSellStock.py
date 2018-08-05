'''
@author  : kongweikun
@file    : 121bestTimeToBuyAndSellStock.py
@time    : 18-7-2 下午10:49
@contact : kongwiki@163.com
'''
import sys

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    dicPrice = {}
    for index, price in enumerate(prices):
        dicPrice.setdefault(price, index)
    b = sorted(prices)
    minIndex = dicPrice[b[0]]
    count = len(prices) - 1
    if count == minIndex:
        return 0
    while dicPrice[b[count]] < minIndex:
        count -= 1
    return dicPrice[b[count]] + 1

"""
动态规划
"""
def maxProfit1(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 0:
        return 0
    minPrice = prices[0]
    maxProfit = 0
    for p in prices:
        if p < minPrice:
            minPrice = p
        elif p - minPrice > maxProfit:
            maxProfit = p - minPrice
    return maxProfit

"""
最优解
"""
def maxProfit2(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0

    max_prof = 0
    min_p = sys.maxsize

    for i in range(len(prices)):
        if prices[i] < min_p:
            min_p = prices[i]
        elif prices[i] - min_p > max_prof:
            max_prof = prices[i] - min_p

    return max_prof


if __name__ == '__main__':
    b = [7,1,5,3,6,4]
    c = [7,6,4,3,1]
    print(maxProfit2(c))
