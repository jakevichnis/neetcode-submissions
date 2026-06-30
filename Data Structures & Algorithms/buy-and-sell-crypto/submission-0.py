class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxProfit = 0
        window_sum = 0
        for i in range(len(prices)):
            if prices[i] > prices[left]:
                window_sum = prices[i] - prices[left]
                if window_sum > maxProfit:
                    maxProfit = window_sum
            else:
                left = i
        return maxProfit