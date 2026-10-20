class Solution:
    def maxProfit(self, prices):
        # going to try a different solution here, the main sliding window solution
        # we set the left pointer to become our buying/purchase pointer
        left = 0
        # this will let us keep track of the max profit we can make at any point
        max_profit = 0
        # we set our right pointer to be the sell pointer, which determintes what the price of the stock looking forward will be
        # but this is set during the main iteration, as such:
        for right in range(len(prices)):
            # now we create a profit variable which will calculate the position of what we do on a given day
            # the thoughts/options either being: this is a good day to sell, or this is a good day to buy
            # profit will equal how much our selling can be subtracted from our buying pointers
            profit = prices[right] - prices[left]

            # now we check if right is less than left, this would actually be a better day to buy on (as the price would be lower)
            if prices[right] < prices[left]:
                left = right
            # if our sell side is equal or higher, we take the count of what the profit would be
            elif prices[right] >= prices[left]:
            # and store that under our max profit
                max_profit = max(max_profit, profit)
        # once we are done iterating through, return max_profit
        return max_profit