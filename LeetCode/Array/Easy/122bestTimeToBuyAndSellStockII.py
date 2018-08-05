'''
@author  : kongweikun
@file    : 122bestTimeToBuyAndSellStockII.py
@time    : 18-7-10 下午7:40
@contact : kongwiki@163.com
'''
"""
design an algorithm to find the maximum profit, You may complete as 
many transactions as you like(buy one and sell one share of the stock
multiple times).
examples 
input [7,1,5,3,6]
output 7
buy on day 2 sell on day 3(profit=4) buy on day 4 sell on day 5(profit=3)
total profit = 7
每一小段价格上升的区间买
"""

def maxProfit(prices):
    """
    :type
    :rtype:
    """
    if not prices:
        return 0
    profit = 0
    low = high = prices[0]
    for i in range(1,len(prices)):
        if prices[i] >= prices[i-1]:
            high = prices[i]
        else:
            profit += high - low
            low = high = prices[i]
    profit += high - low
    return profit


if __name__ == '__main__':
    a = [7,1,5,3,6,4]
    print(maxProfit(a))
    # assert maxProfit(a) == 7

