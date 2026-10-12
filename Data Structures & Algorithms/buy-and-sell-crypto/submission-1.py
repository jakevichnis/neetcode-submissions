class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # record max profit
        # as we iterate we ask the question, is this profit greater or lesser, if so we log it
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit