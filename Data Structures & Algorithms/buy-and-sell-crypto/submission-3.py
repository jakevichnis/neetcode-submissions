class Solution:
    def maxProfit(self, prices):
        left = 0
        minimum = float("inf")
        max_P = float("-inf")
        for right in range(len(prices)):
            profit = prices[right] - prices[left]
            if prices[right] < prices[left]:
                left = right
            max_P = max(max_P, profit)
        return max_P
        