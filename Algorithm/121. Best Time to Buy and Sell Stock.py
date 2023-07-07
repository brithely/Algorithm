"""
2023.07.07
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Easy
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_list = [0] * (len(prices) - 1)
        min_price = prices[0]
        max_profit = 0
        for i, price in enumerate(prices[1:]):
            if min_price > price:
                profit_list[i] = 0
                min_price = price
            else:
                profit_list[i] = price - min_price
        if profit_list:
            max_profit = max(profit_list)
        return max_profit

